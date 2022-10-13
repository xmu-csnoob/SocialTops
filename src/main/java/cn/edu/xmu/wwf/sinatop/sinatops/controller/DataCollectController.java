package cn.edu.xmu.wwf.sinatop.sinatops.controller;

import cn.edu.xmu.wwf.sinatop.sinatops.mapper.DataCollectMapper;
import cn.edu.xmu.wwf.sinatop.sinatops.model.TopRecordPo;
import cn.edu.xmu.wwf.sinatop.sinatops.utils.PythonScriptCaller;
import cn.edu.xmu.wwf.sinatop.sinatops.utils.PythonScripts;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.ClassPathResource;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.web.bind.annotation.RestController;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.LocalDateTime;

/**
 * @author wangwenfei
 * @version 1.0 2022/10/11 增加API：collectDataFromSina
 * @version 2.0 2022/10/13 增加API：collectDataFromZhihu
 *                         修改各样命名
 */
@RestController
public class DataCollectController {
    /**
     * @apiNote 一分钟执行一次，从新浪微博Top50热搜榜采集数据
     */
    @Autowired
    DataCollectMapper dataCollectMapper;
    @Scheduled(cron="0/60000 * *  * * ? ")
    public void collectDataFromSina() throws IOException, InterruptedException {
        PythonScriptCaller.creeper(PythonScripts.SINA_WEIBO_CREEPER);
        // 创建 reader
        UploadDataFromStaticFile("sina.csv");
    }
    @Scheduled(cron="0/60000 * *  * * ? ")
    public void collectDataFromZhihu() throws IOException, InterruptedException {
        PythonScriptCaller.creeper(PythonScripts.ZHIHU_CREEPER);
        // 创建 reader
        UploadDataFromStaticFile("zhihu.csv");
    }

    private void UploadDataFromStaticFile(String path) {
        try (BufferedReader br = Files.newBufferedReader(Paths.get(path))) {
            // CSV文件的分隔符
            String DELIMITER = ",";
            // 按行读取
            String line;
            while ((line = br.readLine()) != null) {
                // 分割
                String[] columns = line.split(DELIMITER);
                // 打印行
                TopRecordPo topRecordPo=new TopRecordPo(columns[0],Integer.parseInt(columns[1]),columns[2],Double.parseDouble(columns[3]),columns[4]);
                dataCollectMapper.insertTopRecord(topRecordPo);
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
