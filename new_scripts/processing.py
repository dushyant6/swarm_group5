#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 18:26:30 2023

@author: dushyant
"""

def resulting_string(x_dict, id):
        res = str(id)
        for key in x_dict:
                print(key)
                dist = x_dict[key]
                res += "," + str(key) + "," + str(dist)
        print(res)
'''
#equivalent function in buzz
function res_string(id, neigh_table){
        res = string.tostring(id)
        res = string.concat(res, " sees neighbors: ")
        foreach(t, function(key,value){
                res = string.concat(res, ",", string.tostring(key), ",", string.tostring(value))
                }

        )
        return res
        }

'''

a = {}
id = 2
a[1] = 12
a[2] = 5
a[3] = 32

resulting_string(a, id)

x = "robot_10 sees neighbors: "
print(x.isnumeric())
