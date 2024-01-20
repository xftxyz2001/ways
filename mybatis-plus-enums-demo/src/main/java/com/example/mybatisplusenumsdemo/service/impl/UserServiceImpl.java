package com.example.mybatisplusenumsdemo.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.mybatisplusenumsdemo.domain.User;
import com.example.mybatisplusenumsdemo.mapper.UserMapper;
import com.example.mybatisplusenumsdemo.service.UserService;
import org.springframework.stereotype.Service;

/**
 * @author 25810
 * @description 针对表【t_user】的数据库操作Service实现
 * @createDate 2024-01-20 10:05:50
 */
@Service
public class UserServiceImpl extends ServiceImpl<UserMapper, User>
        implements UserService {

}




