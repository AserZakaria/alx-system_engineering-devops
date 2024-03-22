# 1-install_a_package.pp

# Ensure the package 'python3-pip' is installed
package { 'python3-pip':
  ensure => installed,
}

# Use pip3 to install Flask version 2.1.0
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  # Ensure that the command runs only if Flask is not already installed or is a different version
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'], # Ensure python3-pip is installed before trying to install Flask
}

# Notify to print a message after installation
notify { 'Flask installed successfully':
  subscribe => Exec['install_flask'],
}
