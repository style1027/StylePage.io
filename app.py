from flask import Flask, render_template, request
from sparkai.llm.llm import ChatSparkLLM, ChatMessage

app = Flask(__name__)

# 星火认知大模型Spark Max的配置信息
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v1.1/chat'
SPARKAI_APP_ID = '5bf217d8'  # 请替换为你的实际App ID
SPARKAI_API_SECRET = 'ZDZjZTY0MDg5Y2M0NThlZDRlMzkyYjZl'  # 请替换为你的实际API Secret
SPARKAI_API_KEY = '041c8b11b15c532bfe70a597ab68f340'  # 请替换为你的实际API Key
SPARKAI_DOMAIN = 'lite'  # 根据需要选择合适的domain

# 初始化ChatSparkLLM
spark = ChatSparkLLM(
    spark_api_url=SPARKAI_URL,
    spark_app_id=SPARKAI_APP_ID,
    spark_api_key=SPARKAI_API_KEY,
    spark_api_secret=SPARKAI_API_SECRET,
    spark_llm_domain=SPARKAI_DOMAIN,
    streaming=False,
)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ""
    ai_response = ""
    if request.method == 'POST':
        user_input = request.form['user_input']
        messages = [ChatMessage(role="user", content=user_input)]
        try:
            response = spark.generate([messages])
            # 假设每个消息只有一个生成结果
            ai_response = response.generations[0][0].text  # 获取AI的回答内容
        except Exception as e:
            ai_response = f"发生错误: {str(e)}"
    return render_template('index.html', user_input=user_input, ai_response=ai_response)

if __name__ == '__main__':
    app.run(debug=True)
