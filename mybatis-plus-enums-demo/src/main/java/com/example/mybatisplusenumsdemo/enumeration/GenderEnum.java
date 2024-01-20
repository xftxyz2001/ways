package com.example.mybatisplusenumsdemo.enumeration;

import com.baomidou.mybatisplus.annotation.EnumValue;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonValue;
import lombok.AllArgsConstructor;
import lombok.Getter;

@AllArgsConstructor
@Getter
// @JsonFormat(shape= JsonFormat.Shape.OBJECT)
public enum GenderEnum {

    MALE(1, "男"),
    FEMALE(0, "女"),
    UNKNOWN(-1, "未知");

    @EnumValue // 标记数据库的存储字段
    private final Integer code;

    @JsonValue // 标记序列化时的值
    private final String name;

    @JsonCreator // 标记反序列化时的构造方法（如果没有这个注解，反序列化时会使用@JsonValue标记的字段进行映射）
    public static GenderEnum getEnum(Integer code) {
        for (GenderEnum genderEnum : GenderEnum.values()) {
            if (genderEnum.getCode().equals(code)) {
                return genderEnum;
            }
        }
        return null;
    }

}
