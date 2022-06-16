import readAllFile as raf
import util

dirs = raf.readDir("C:/Users/ren.cai/Desktop/工作文件/0615excel")
for path in dirs:
    util.deal_and_save(path)
