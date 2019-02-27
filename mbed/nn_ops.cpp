#include "nn_ops.hpp"





void conv_2d(float* in, float* out, float* kernel, int k_size, int in_size, int in_depth) {
    int out_size = in_size - k_size + 1;
    // in column direction
    for (int i = 0; i < out_size; i++) {
        // in row direction
        for (int j = 0; j < out_size; j++) {
            // convolvution
            float sum = 0;
            for (int k = 0; k < k_size; k++) {
                for (int l = 0; l < k_size; l++) {

                    for (int m = 0; m < in_depth; m++) {
                        sum += in[m*in_size*in_size + (i+k)*in_size + (j+l)] * kernel[m*k_size*k_size + k*k_size + l];
                    }


                }
            }
            out[(i)*out_size + (j)] = sum;
        }
    }

    return;
}




void conv_2d_layer(float* in, float* out, float* kernel, int in_size, int k_size, int in_depth, int kernel_depth) {
    int out_size = in_size - k_size + 1;

    for (int i = 0; i < kernel_depth; i++) {
        float* kernel_start = &kernel[i*k_size*k_size*in_depth];
        float* out_start = &out[i*out_size*out_size];

        conv_2d(in, out_start, kernel_start, k_size, in_size, in_depth);
    }

    return;
}




void add_bias(float* input, float* bias, int size, int depth) {
    for (int i = 0 ; i < depth; i++) {
        float current_bias = bias[i];
        for (int j = 0; j < size*size; j++) {
            input[i*size*size+j] += current_bias;
        }
    }
}




void max_pool_2d(float* input, float* output, int input_side_length, int num_input_channels, int pool_size) {
    int i, j, k, m, n;
    float max = -99999;
    int chunk = input_side_length / pool_size;
    int count = 0;

    for (i = 0; i < num_input_channels; i++) {
        for (j = 0; j < chunk; j++) {
            for (k = 0; k < chunk; k++) {
                for (m = 0; m < pool_size; m++) {
                    for (n = 0; n < pool_size; n++) {
                        float temp = input[i * input_side_length * input_side_length + j * chunk * pool_size * pool_size + k * pool_size + input_side_length * m + n];
                        if (temp > max) {
                            max = temp;
                        }
                    }
                }
            output[count] = max;
            max = -99999;
            count = count + 1;
            }
        }
    }
}


void relu(float* input, int size, int depth) {
    for (int i = 0 ; i < depth; i++) {
        for (int j = 0; j < size*size; j++) {
            if (input[i*size*size+j] < 0) {
                input[i*size*size+j] = 0;
            }
        }
    }
}


void mat_mul(float* matrix, float* vector, float* output, int matrix_l, int matrix_w) {
    for (int i = 0; i < matrix_l; i++) {
        float sum = 0;
        for (int j = 0; j < matrix_w; j++) {
            sum += matrix[i*matrix_w + j] * vector[j];
        }
        output[i] = sum;
    }
}
