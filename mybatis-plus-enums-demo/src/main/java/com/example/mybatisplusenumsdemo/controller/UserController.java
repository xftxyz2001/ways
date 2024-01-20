package com.example.mybatisplusenumsdemo.controller;

import com.example.mybatisplusenumsdemo.domain.User;
import com.example.mybatisplusenumsdemo.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/user")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @GetMapping("/list")
    public List<User> getUserList() {
        return userService.list();
    }

    @GetMapping("/{id}")
    public User getUserById(@PathVariable("id") Long id) {
        return userService.getById(id);
    }

    @PostMapping("/save")
    public boolean saveUser(@RequestBody User user) {
        return userService.save(user);
    }

    @PutMapping("/update")
    public boolean updateUser(@RequestBody User user) {
        return userService.updateById(user);
    }

    @DeleteMapping("/{id}")
    public boolean deleteUser(@PathVariable("id") Long id) {
        return userService.removeById(id);
    }
}
