import tkinter as tk
from tkinter import ttk

import math
from math import *

import ast
from ast import *

# 自定义函数，计算平方
def OWN(x):
    return x * x


class CalculatorApp:
    def __init__(self, root):
        self.root = root

        root.configure(bg="red")    # 设置红色背景
        root.geometry("450x60")    # 设置大小



        root.title("新年快乐，龙年大吉")  # 设置窗口标题




        # 创建输入表达式的标签和输入框
        self.input_label = tk.Label(root, text="输入:", width=4, height=1)
        self.input_label.grid(row=0, column=0, sticky=tk.W)

        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.grid(row=0, column=1, columnspan=2)

        # 创建显示结果的标签和输出框
        self.result_label = tk.Label(root, text="结果:", width=4, height=1)
        self.result_label.grid(row=1, column=0, sticky=tk.W)

        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(root, textvariable=self.result_var, state='readonly', width=50)
        self.result_entry.grid(row=1, column=1, columnspan=2)

        # 创建计算按钮，并绑定计算方法
        self.calculate_button = tk.Button(root, text="计算", width=10, height=1, command=self.calculate)
        self.calculate_button.grid(row=0, column=3, columnspan=2)

    # 计算方法，获取表达式并计算结果
    def calculate(self):
        expression = self.input_entry.get()
        try:
            result = self.evaluate_expression(expression)
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")

    # 解析表达式为语法树
    def parse_expression(self, expression):
        return ast.parse(expression, mode='eval').body

    # 对语法树进行求值
    def evaluate_expression(self, expression):
        syntax_tree = self.parse_expression(expression)
        return self.evaluate_syntax_tree(syntax_tree)

    # 遍历语法树并递归求值
    def evaluate_syntax_tree(self, syntax_tree):
        if isinstance(syntax_tree, ast.Num):  # 数字节点
            return syntax_tree.n

        elif isinstance(syntax_tree, ast.BinOp):  # 二元运算节点
            left_value = self.evaluate_syntax_tree(syntax_tree.left)
            right_value = self.evaluate_syntax_tree(syntax_tree.right)

            if isinstance(syntax_tree.op, ast.Add):  # 加法
                return left_value + right_value
            elif isinstance(syntax_tree.op, ast.Sub):  # 减法
                return left_value - right_value
            elif isinstance(syntax_tree.op, ast.Mult):  # 乘法
                return left_value * right_value
            elif isinstance(syntax_tree.op, ast.Div):  # 除法
                return left_value / right_value

            elif isinstance(syntax_tree.op, ast.FloorDiv):  # 整除
                return left_value // right_value
            elif isinstance(syntax_tree.op, ast.Mod):  # 求模
                return left_value % right_value
            elif isinstance(syntax_tree.op, ast.Pow):  # 乘方
                return left_value ** right_value

        elif isinstance(syntax_tree, ast.Call):  # 函数调用节点
            func_name = syntax_tree.func.id
            arg_value = self.evaluate_syntax_tree(syntax_tree.args[0])
            if func_name == 'sin':  # sin函数
                return math.sin(arg_value)
            elif func_name == 'cos':  # cos函数
                return math.cos(arg_value)
            elif func_name == 'sqrt':  # 开方函数
                return math.sqrt(arg_value)


            elif func_name == 'OWN':  # 自定义的OWN函数（计算平方）
                return OWN(arg_value)


            elif func_name == 'tan':  # tan函数
                return math.tan(arg_value)
            elif func_name == 'asin':  # asin函数
                return math.asin(arg_value)
            elif func_name == 'acos':  # acos函数
                return math.acos(arg_value)
            elif func_name == 'atan':  # atan函数
                return math.atan(arg_value)
            elif func_name == 'ln':  # ln函数
                return math.log(arg_value)
            elif func_name == 'log':  # log=ln
                return math.log(arg_value)
            elif func_name == 'lg':  # lg函数
                return math.log10(arg_value)
            # 添加自己喜欢的函数


        elif isinstance(syntax_tree, ast.Name):
            if syntax_tree.id == 'pi':      # 加入常数pi
                return math.pi
            elif syntax_tree.id == 'e':     # 加入常数e
                return math.e

        else:
            raise ValueError("Unsupported operation")  # 不支持的操作

    # 希望你不必纠结于pi和π
    def parse_expression(self, expression):
        # 将π替换为pi
        expression = expression.replace("π", "pi")
        return ast.parse(expression, mode='eval').body


if __name__ == "__main__":
    root = tk.Tk()  # 创建窗口
    app = CalculatorApp(root)  # 创建应用程序实例
    root.mainloop()  # 运行主事件循环
