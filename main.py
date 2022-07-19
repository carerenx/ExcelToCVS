import readAllFile as raf
import util

dirs = raf.readDir("./0615excel")
for path in dirs:
    util.deal_and_save(path)
