package cn.edu.xmu.wwf.sinatop.sinatops.model;


import lombok.AllArgsConstructor;
import lombok.Data;

import java.time.LocalDateTime;

@Data
public class TopRecordPo {
    int id;
    String title;
    int ranking;
    String time;
    double popularity;
    String platform;
    public TopRecordPo(String title,int ranking,String time,double popularity,String platform){
        this.title=title;
        this.ranking=ranking;
        this.time=time;
        this.popularity=popularity;
        this.platform=platform;
    }
}
