#pragma once

#include "wire.pb.h"

namespace is {

wire::Status make_status(wire::StatusCode code, std::string const& why = "");

}  // namespace is