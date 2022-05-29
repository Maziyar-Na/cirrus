#ifndef MLUTILS_H_
#define MLUTILS_H_

#include <cmath>
#include <string>
#include <stdexcept>
#include <iostream>
namespace cirrus {

/**
  * Computes safe sigmoid of value x
  * @param x Input value
  * @return Sigmoid of x
  */
float s_1_float(float x);

template<typename T>
T s_1(T x) {
    std::cerr << "[dbg][WORKER] s_1, beginning calculating sigmoid . . ." << std::endl;
    std::cerr << "[dbg][WORKER] s_1, exponential of input: " << std::exp(-x) <<std::endl;
    double res = 1.0 / (1.0 + std::exp(-x));
    std::cerr << "[dbg][WORKER] s_1, result of the sigmoid calculation: " << res << std::endl;
    if (std::isnan(res) || std::isinf(res)) {
        throw std::runtime_error(
                std::string("s_1 generated nan/inf x: " + std::to_string(x)
                    + " res: " + std::to_string(res)));
    }
    return res;
}

/**
  * Computes logarithm
  * Check for NaN and Inf values
  * Clip values if they are too small (can lead to problems)
  * @param x Input value
  * @return Logarithm of x
  */
double log_aux(double x);

}  // namespace mlutils

#endif  // MLUTILS_H_
