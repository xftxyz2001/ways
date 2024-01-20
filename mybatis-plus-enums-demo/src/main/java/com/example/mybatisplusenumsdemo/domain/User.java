package com.example.mybatisplusenumsdemo.domain;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import com.example.mybatisplusenumsdemo.enumeration.GenderEnum;
import lombok.Data;

import java.io.Serializable;

/**
 * @TableName t_user
 */
@TableName(value = "t_user")
@Data
public class User implements Serializable {
    /**
     *
     */
    @TableId(value = "id", type = IdType.AUTO)
    private Long id;

    /**
     *
     */
    @TableField(value = "uname")
    private String uname;

    /**
     *
     */
    @TableField(value = "gender")
    private GenderEnum gender;

    @TableField(exist = false)
    private static final long serialVersionUID = 1L;
}