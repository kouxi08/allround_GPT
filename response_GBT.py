import openai
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

res = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   messages=[
       # １回目の質問　※１回の処理につき、１つの返答のみ
       {
           "role": "system",
           "content": "日本語で返答してください。"
       },
       {
           "role": "user",
           "content": "What is AI?"
       },
        # ２回目の質問
        {
           "role": "assistant",
           "content": "AIとは、人工知能(artificial intelligence)のことです。コンピューターやロボットなどに人間と同じように思考・判断・学習などの能力を与える技術や分野を示します。AI技術は、様々な分野で応用されており、自動運転車、言語処理、画像認識、医療など、私たちの生活に多大な影響を与えています。"
       },
       {
           "role": "user",
           "content": "英語に翻訳してください。"
       },
         # ３回目の質問　※1,2回目の処理は無視されて最後の(3回目)処理がされる
        {
           "role": "assistant",
           "content": "AIとは、人工知能(artificial intelligence)のことです。コンピューターやロボットなどに人間と同じように思考・判断・学習などの能力を与える技術や分野を示します。AI技術は、様々な分野で応用されており、自動運転車、言語処理、画像認識、医療など、私たちの生活に多大な影響を与えています。"
       },
       {
           "role": "user",
           "content": "ギャルっぽく返答してください。"
       },
   ],
)
# print(res)　←　これは、データ全体を表示する・別になくてもいい
print(res["choices"][0]["message"]["content"])