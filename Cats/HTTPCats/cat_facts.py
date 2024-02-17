import cat_wrapper_implemented

facts_url = 'https://cat-fact.herokuapp.com/facts'

facts = cat_wrapper.get(facts_url).json()
cat_wrapper.get(facts_url + "/dogs")
cat_wrapper.post(facts_url)

for fact in facts:
    print(f"- {fact['text']}")
