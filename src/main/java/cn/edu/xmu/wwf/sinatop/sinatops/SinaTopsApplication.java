package cn.edu.xmu.wwf.sinatop.sinatops;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class SinaTopsApplication {
    public static void main(String[] args) {
        SpringApplication.run(SinaTopsApplication.class, args);
    }

}
