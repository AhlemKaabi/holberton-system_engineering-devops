# Using strace, find out why Apache is returning a 500 error.
#  ps auxw | grep sbin/apache | awk '{print"-p " $2}' | xargs strace 
# sed -i 's/old-text/new-text/g' input.txt
exec {'fix_wordpress':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
