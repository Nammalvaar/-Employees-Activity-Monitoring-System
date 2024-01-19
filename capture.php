<?php

include("../components/function.php");

if (isset($_POST['capture'])) {
    $empl_id = $_POST['empl_id'];
    $duration = $_POST['duration'];

    $command = "python testing.py " . escapeshellarg($empl_id) . " " . escapeshellarg($duration);

    $output = shell_exec($command);

    echo $output; 
}

?>