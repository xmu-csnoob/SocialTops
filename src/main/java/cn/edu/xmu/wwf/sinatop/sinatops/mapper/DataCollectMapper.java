package cn.edu.xmu.wwf.sinatop.sinatops.mapper;

import cn.edu.xmu.wwf.sinatop.sinatops.model.TopRecordPo;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface DataCollectMapper {
    void insertTopRecord(TopRecordPo topRecordPo);
}
