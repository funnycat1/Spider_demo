# 获取《西游记》的所有章节信息：https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}
# 获取《西游记》的每个章节原文：https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}

# getCatalog 获取所有章节的 cid 和 title -- 同步操作
# getChapterContent 通过 book_id，cid，title 获取每个章节原文 -- 异步操作
# 新见文件写入章节原文时也是 io 操作，也可以异步操作，使用协程

import json
import requests
import asyncio
import aiohttp
import aiofiles


async def getCatalog(url):
    """
    :param url: 小说的所有章节信息地址
    :return: 小说的所有章节
    """
    resp = requests.get(url)
    # print(resp.json())
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        # print(item)
        title = item['title']
        cid = item['cid']
        tasks.append(getChapterContent(book_id, cid, title))

    await asyncio.wait(tasks)


async def getChapterContent(book_id, cid, title):
    """
    :param book_id: 书id
    :param cid: 章节id
    :param title: 章节名称
    :return: 章节对应的原文
    """
    data = {
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open("../novel/xyj/"+title, mode='w', encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])


if __name__ == '__main__':

    book_id = '4306063500'
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":' + book_id + '}'
    # print(url)
    asyncio.get_event_loop().run_until_complete(getCatalog(url))

    print("well, done")
