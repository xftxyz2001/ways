package com.example.mybatisplusenumsdemo;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.example.mybatisplusenumsdemo.mapper")
public class MybatisPlusEnumsDemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(MybatisPlusEnumsDemoApplication.class, args);
    }

}
