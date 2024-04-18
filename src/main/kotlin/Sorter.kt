package org.example

fun interface Sorter<T: Comparable<T>> {
    fun sort(list: MutableList<T>)
}