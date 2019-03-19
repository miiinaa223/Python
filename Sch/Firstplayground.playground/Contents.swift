//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"
var sum = 0
/// sum =はsumというデータの入れ物を定義
for i in 1...10 {
/// iを10回繰り返す
    sum += i
///+=右側の値を左側の数に足す
}

var height:Int = 180
var weight = 70
height + weight
let dayOfYear:Int = 365

var str1 = "Hello, "
var str2 = "Swift"
str1 + str2

var num1 = 10 // 整数(int型)
var num2 = 5.5 //Double型(小数点含)
// num1 + num2 // (型が違うと計算不可能)
Double(num1) + num2 //型変換(castする。) double型に揃えた。

var num3 = 123 //整数ー>文字列にする
var str3 = "Swift" //文字列
// num3 + str3 型が違う

String(num3) + "! " + str3

// 整数 Int
// 浮動小数点数・実数 Double
// 文字列 String
// ブール型 True or False


// 文字列から整数に変換する場合はアンラップの処理が必要 ?=オプショナル値。
var str5 = "1234"
// var int1 = Int(str5) //変換
var int1:Int? = Int(str5)
//オプショナル変数を解除して値を取り出す。あんラップする var!
var int2 = 2345
int1! + int2
// nil or null オプショナル型の変数(niが入る可能性のある変数)



// 配列・アレー・Array. アレーは全て同じ文字の種類である必要がある。
var numbers = [1,2,3,4,5] //複数の数字を一つの名前で呼ぶ=numbers
var dayWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satday", "Sunday"]
dayWeek[2] // 添字
numbers[4]
var dayWeek_JP = ["月", "火", "水", "木", "金", "土", "日"]
dayWeek_JP[3]






