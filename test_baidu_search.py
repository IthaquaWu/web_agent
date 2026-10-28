from playwright.sync_api import sync_playwright
import time


def test_baidu_search():
    # 启动 Playwright
    with sync_playwright() as p:
        # 选择浏览器（chromium/firefox/webkit）
        browser = p.chromium.launch(
            headless=False,  # 设置为 True 则无头模式（不显示浏览器界面）
            slow_mo=500,  # 操作延迟 500ms（便于观察）
            timeout=60000  # 超时时间 60 秒
        )

        try:
            # 创建新页面
            page = browser.new_page()

            # 访问百度
            page.goto("https://www.baidu.com")
            print("✅ 已打开百度首页")

            # 截图保存（可选）
            #page.screenshot(path="baidu_homepage.png", full_page=True)
            #print("✅ 已保存截图到 baidu_homepage.png")

            # 在搜索框输入关键词并搜索
            page.fill('input[id="kw"]', "Playwright 自动化测试")
            page.click('input[id="su"]')  # 点击搜索按钮
            print("✅ 已提交搜索请求")

            # 等待搜索结果加载（通过选择器判断）
            page.wait_for_selector('div[id="content_left"]', timeout=10000)
            print("✅ 搜索结果已加载")

            # 打印当前页面标题
            print(f"当前页面标题: {page.title()}")

            # 暂停 5 秒观察结果（仅调试用）
            time.sleep(5)

        except Exception as e:
            print(f"❌ 发生错误: {str(e)}")
        finally:
            # 关闭浏览器
            browser.close()
            print("✅ 浏览器已关闭")


if __name__ == "__main__":
    test_baidu_search()