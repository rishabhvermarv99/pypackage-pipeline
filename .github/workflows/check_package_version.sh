#!/bin/bash

# Define the package name you want to check
package_name="django"

# Use pip to fetch the package information
package_info=$(pip show $package_name)
echo "$package_info"
# Extract and display the package version
package_version=$(echo "$package_info")
# echo "Package Version: $package_version"
curl -s "https://pypi.org/pypi/sigmoidpythonpackage/json" | jq -r '.info.version'