#!/usr/bin/env perl

use v5.10;
use strict;

# TODO: frameset для ебач2 -- скрытая шторка снизу
 
my $q = $ENV{QUERY_STRING};
$q||='index';
my $styleHome = $q;
my $styleCurr = '';
if ($q eq 'stuff' || $q eq 'me') {$styleCurr = 'active'; $styleHome = 'home'} else {$styleHome = 'index'};

print <<"END";
<!-- что тебе тут надо spurdo sarde dolores sit ame lorem ipsum muspi esup! -->

<!DOCTYPE html>
<html>
  <head>
    <title>krasn0glaz</title>
	<meta name="keywords" content="krasn0glaz illia bilyk trance goatrance psytrance psy techno rave braindance idm ambient tape expreimental">
	<meta charset="UTF-8">
	<meta name="description" content="official site.  music/merch/photos/etc.">
	<link rel=stylesheet type='text/css' media=screen href='/style.css'><link rel="icon" href="favicon.ico" type="image/x-icon" />
  </head>
  <body>
	<div class="header">
    	<a class="$styleHome" href="/">krasn0glaz</a>
		<a class="@{[do{if ($q eq 'stuff') {$styleCurr}}]}" href="/?stuff">stuff</a><a class="@{[do{if ($q eq 'me') {$styleCurr}}]}" href="/?me">me</a><a class="board" href="/board/">ebach</a>
  </div>
END

my $file = "$q/index.html";
if (open(my $fh, '<:encoding(UTF-8)', $file)) {
  while (my $row = <$fh>) {
    chomp $row;
    print "$row\n";
  }};

print <<"END";
	<footer><a class="secret" href="/board2">:x!</a></footer>
  </body>
</html>
END
