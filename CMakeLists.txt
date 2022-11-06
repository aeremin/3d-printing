cmake_minimum_required(VERSION 3.20)

# set the project name
project(3D_Printing)

include(FetchContent)
cmake_policy(SET CMP0135 NEW)


add_subdirectory(Board\ games)
add_subdirectory(Painting)
add_subdirectory(Sports)
add_subdirectory(3D\ Printer)
add_subdirectory(Apartment)