package cn.edu.xmu.wwf.sinatop.sinatops.utils;

public enum PythonScripts {
    SINA_WEIBO_CREEPER("新浪微博","classes/sina_creeper.py"),
    ZHIHU_CREEPER("知乎","classes/zhihu_creeper.py");
    private String name;
    private String path;
    PythonScripts(String name,String path){
        this.name=name;
        this.path=path;
    }
    public String getName(){
        return name;
    }
    public String getPath(){
        return path;
    }
}
