package cn.edu.xmu.wwf.sinatop.sinatops.utils;

import lombok.experimental.UtilityClass;

import java.io.IOException;

@UtilityClass
public class PythonScriptCaller {
    public static void creeper(PythonScripts pythonScripts) throws IOException, InterruptedException {
        final ProcessBuilder processBuilder = new ProcessBuilder("python3",pythonScripts.getPath());
        processBuilder.redirectErrorStream(true);
        final Process process = processBuilder.start();
        final int exitCode = process.waitFor();
        System.out.println("爬虫运行情况报告:"+(exitCode == 0));
    }
}
