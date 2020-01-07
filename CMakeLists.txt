cmake_minimum_required(VERSION 3.9)
project(word_num_array)

set(CMAKE_C_STANDARD 99)
set(SOURCE_FILES word_num_array/main.c
        word_num_array/get_words.c
        word_num_array/dump_word.c
        word_num_array/add_word.c
        word_num_array/initialize.c
        word_num_array/finalize.c
        )


add_executable(word_num_array ${SOURCE_FILES})