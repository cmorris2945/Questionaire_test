# Use the official PHP Apache image
FROM php:8.1-apache

# Update package list and install prerequisites
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    apt-transport-https \
    libc6 libstdc++6 \
    libkrb5-3

# Add Microsoft repository for ODBC driver
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl -sSL https://packages.microsoft.com/config/debian/11/prod.list -o /etc/apt/sources.list.d/mssql-release.list

# Remove potentially conflicting packages if they exist
RUN apt-get purge -y unixodbc-dev odbcinst libodbc1 && apt-get update

# Install unixodbc and msodbcsql17
RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y \
    unixodbc \
    msodbcsql17

# Now install unixodbc-dev
RUN apt-get install -y unixodbc-dev

# Install sqlsrv and pdo_sqlsrv PHP extensions
RUN pecl install sqlsrv pdo_sqlsrv && \
    docker-php-ext-enable sqlsrv pdo_sqlsrv

# Clean up to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the PHP application code into the container
COPY . /var/www/html/

# Set the working directory
WORKDIR /var/www/html

# Set the permissions (optional)
RUN chown -R www-data:www-data /var/www/html

# Expose the port that Apache is running on
EXPOSE 80

# Start Apache
CMD ["apache2-foreground"]
