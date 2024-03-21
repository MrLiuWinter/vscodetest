cmake_minimum_required(VERSION 3.15.0)
project(HelloWorld CXX)

# C++标准
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)  # C++ 11 是强制要求，不会衰退至低版本
set(CMAKE_CXX_EXTENSIONS OFF)        # 禁止使用编译器特有扩展

# Debug编译后缀
set(CMAKE_DEBUG_POSTFIX d)

# Find architecture property
if(CMAKE_SIZEOF_VOID_P EQUAL 8)
    set(PROJECT_ARCH_TARGET "amd64")    # x64
elseif(CMAKE_SIZEOF_VOID_P EQUAL 4)
    set(PROJECT_ARCH_TARGET "i386")     # x86
else()
    message(FATAL_ERROR "Unkwnown architecture, CMake will exit.")
endif()

# 根目录
set(ROOTPATH ${PROJECT_SOURCE_DIR})
set(BUILDPATH ${PROJECT_BINARY_DIR})
message("构建目录：" ${PROJECT_BINARY_DIR})
set(INCPATH ${ROOTPATH}/include)
set(LIBPATH ${ROOTPATH}/lib)

# 全局包含
include_directories(${INCPATH}
${DEPPATH}/include)
link_directories(${DEPPATH}/lib
${DEPPATH}/lib/ffmpeg_sdl)

# 设置不同编译器选项
if (${CMAKE_CXX_COMPILER_ID} STREQUAL MSVC)
    set(CMAKE_BUILD_TYPE Debug)
    add_compile_options(/MP /wd4819 /std:c++20 /Zc:__cplusplus /utf-8)
elseif (${CMAKE_CXX_COMPILER_ID} STREQUAL GNU)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++2a -Wall")
elseif (${CMAKE_CXX_COMPILER_ID} STREQUAL Clang)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++2a -Wall")
endif ()

# 设置生成目录
if (MSVC)
    set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_DEBUG ${BUILDPATH}/Debug/lib)
    set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_DEBUG ${BUILDPATH}/Debug/lib)
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG ${BUILDPATH}/Debug/bin)
    set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE ${BUILDPATH}/Release/lib)
    set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_RELEASE ${BUILDPATH}/Release/lib)
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${BUILDPATH}/Release/bin)
else ()
    set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${BUILDPATH}/${CMAKE_BUILD_TYPE}/lib)
    set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${BUILDPATH}/${CMAKE_BUILD_TYPE}/lib)
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${BUILDPATH}/${CMAKE_BUILD_TYPE}/bin)
endif()


add_executable(HelloWorld main.cpp)

# 测试模块
# include(CTest)
#enable_testing()
# 打包模块
# set(CPACK_PROJECT_NAME ${PROJECT_NAME})
# set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
# include(CPack)