#!/usr/bin/env perl

use v5.10;
use strict;

my $q = $ENV{QUERY_STRING};
$q||='index';
my $styleHome = $q;
my $styleCurr = '';
if ($q eq 'stuff' || $q eq 'me') {$styleCurr = 'active'; $styleHome = 'home'} else {$styleHome = 'index'};

print <<"END";
<!-- что тебе тут надо spurdo sarde dolores sit ame lorem ipsum muspi esup! -->

<!DOCTYPE html>
<html>
  <head>  <meta charset="UTF-8">
	<meta name="keywords" content="krasn0glaz illia bilyk trance goatrance psytrance psy techno rave braindance idm ambient tape expreimental">
	<meta name="description" content="official site.  music/merch/photos/etc.">
	<link rel=stylesheet type='text/css' media=screen href='/style.css'><link rel="icon" href="favicon.ico" type="image/x-icon" />
END

my $file = "index.html";
if (open(my $fh, '<:encoding(UTF-8)', $file)) {
  while (my $row = <$fh>) {
    chomp $row;
    print "$row\n";
  }};

my $file = "footer.html";
if (open(my $fh, '<:encoding(UTF-8)', $file)) {
  while (my $row = <$fh>) {
    chomp $row;
    print "$row\n";
  }};


print <<"END";
  </body>
</html>
END
