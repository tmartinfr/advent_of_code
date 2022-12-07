<?php

function init_stacks($graph_stack) {
    $stacks = [];
    for($i = 0; $i < 9; ++$i) {
        $stacks[$i] = [];
    }

    foreach(array_reverse(explode("\n", rtrim($graph_stack))) as $line) {
        if(substr($line, 0, 2) == ' 1') {
            continue;
        }
        for($i = 0; $i < (strlen($line) - 1) / 4; ++$i) {
            $c_offset = 4 * $i + 1;
            $c = substr($line, $c_offset, 1);
            if($c == ' ') {
                continue;
            }
            $stacks[$i][] = $c;
        }
    }

    return $stacks;
}

function print_res($stacks) {
    $res = '';
    foreach($stacks as $s) {
        $res .= end($s);
    }

    print($res."\n");
}

$fd = file_get_contents("05_input");
[$graph_stack, $graph_move] = explode("\n\n", $fd);

$stacks = init_stacks($graph_stack);
$moves = [];

foreach(explode("\n", rtrim($graph_move)) as $line) {
    if(preg_match('/move (\d+) from (\d+) to (\d+)/', $line, $m)) {
        $moves[] = [$m[1], $m[2], $m[3]];
    }
}

foreach($moves as $m) {
    for($i = 0; $i < $m[0]; ++$i) {
        $elem = array_pop($stacks[$m[1] - 1]);
        $stacks[$m[2] - 1][] = $elem;
    }
}

print_res($stacks);

$stacks = init_stacks($graph_stack);

foreach($moves as $m) {
    $tmp = [];
    for($i = 0; $i < $m[0]; ++$i) {
        $tmp[] = array_pop($stacks[$m[1] - 1]);
    }
    array_reverse($tmp);
    for($i = 0; $i < $m[0]; ++$i) {
        $stacks[$m[2] - 1][] = array_pop($tmp);
    }
}

print_res($stacks);
