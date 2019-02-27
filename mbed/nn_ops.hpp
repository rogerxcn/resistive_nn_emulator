#ifndef NN_OPS_HPP_
#define NN_OPS_HPP_ 1

#include <cstring>
#include <stdlib.h>

void conv_2d(float* in, float* out, float* kernel, int k_size, int in_size, int in_depth);
void conv_2d_layer(float* in, float* out, float* kernel, int k_size, int in_size, int in_depth, int kernel_depth);

void add_bias(float* input, float* bias, int size, int depth);

void max_pool_2d(float* input, float* output, int input_side_length, int num_input_channels, int pool_size);

void relu(float* input, int size, int depth);

void mat_mul(float* matrix, float* vector, float* output, int matrix_l, int matrix_w);

#endif
