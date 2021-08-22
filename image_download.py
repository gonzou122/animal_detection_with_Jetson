from icrawler.builtin import GoogleImageCrawler　#←googleやBingを選択可能
crawler = GoogleImageCrawler(storage={"root_dir": "<作成される画像格納用のフォルダ名>"})
crawler.crawl(keyword="<検索ワード>", max_num=100)
