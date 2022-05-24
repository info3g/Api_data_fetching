#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests,json,time
Api = requests.get('https://api.scryfall.com/catalog/card-names')
Api_data = Api.json()['data']
for i in Api_data:
    output = requests.get('https://api.scryfall.com/cards/named?fuzzy='+str(i))
    print(output.json())
    time.sleep(3)
    print("***********************************")


# In[ ]:





# In[278]:


# Import library
import mysql.connector,requests,json,time

# funtion call
def Scryfall():
    # Database connectivity
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database='scryfall_apis')
    cursor = mydb.cursor(buffered=True)
    # Fetch all cred name
    Api = requests.get('https://api.scryfall.com/catalog/card-names')
    Api_data = Api.json()['data']
    # All card name send one by one in loop and fetch the infromation
    for i in Api_data:
        output = requests.get('https://api.scryfall.com/cards/named?fuzzy='+str(i))
        list = dict.items(output.json())
        time.sleep(2)
        objects = ''
        ids = ''
        oracle_id = ''
        stroracle_id = ''
        mtgo_id = ''
        multiverse_ids = ''
        name = ''
        lang = ''
        released_at = ''
        uri= ''
        scryfall_uri= ''
        layout= ''
        highres_image= ''
        image_status = ''
        image_uris = ''
        mana_cost = ''
        cmc = ''
        type_line = ''
        oracle_text = ''
        colors = ''
        color_identity = ''
        keywords = ''
        all_parts = ''
        legalities = ''
        games = ''
        reserved = ''
        foil = ''
        nonfoil = ''
        finishes = ''
        oversized = ''
        promo = ''
        reprint = ''
        variation = ''
        set_id = ''
        sets = ''
        set_name = ''
        set_type = ''
        set_uri = ''
        set_search_uri = ''
        scryfall_set_uri = ''
        rulings_uri = ''
        prints_search_uri = ''
        collector_number = ''
        digital = ''
        rarity = ''
        card_back_id = ''
        artist = ''
        artist_ids = ''
        illustration_id = ''
        border_color = ''
        frame = ''
        security_stamp = ''
        full_art = ''
        textless = ''
        booster = ''
        story_spotlight = ''
        prices = ''
        related_uris = ''
        mtgo_foil_id =''
        tcgplayer_id=''
        cardmarket_id=''
        power=''
        toughness=''
        watermark=''
        flavor_text=''
        edhrec_rank=''
        purchase_uris = ''
        # Filter data 
        for i in list:
            if i[0] == 'object':
                objects = i[1]  
            if i[0] == 'id':
                ids = i[1]
                print(ids)
            if i[0] == 'stroracle_id':
                stroracle_id = i[1]
            if  i[0] == 'oracle_id':
                oracle_id = i[1]
            if i[0] == 'multiverse_ids':
                multiverse_ids = i[1]
            if i[0] == 'mtgo_id':
                mtgo_id = i[1]
            if i[0] =='mtgo_foil_id': 
                mtgo_foil_id = i[1]
            if i[0] == 'tcgplayer_id':
                tcgplayer_id = i[1]
            if i[0] == 'cardmarket_id':
                cardmarket_id = i[1]
            if i[0] == 'name':
                name = i[1]
            if i[0] == 'lang':
                lang = i[1]
            if i[0] == 'released_at':
                released_at = i[1]
            if i[0] == 'uri':
                uri = i[1]
            if i[0] == 'scryfall_uri':
                scryfall_uri = i[1]
            if i[0] == 'layout':
                layout = i[1]
            if i[0] == 'highres_image':
                highres_image = i[1]
            if i[0] == 'image_status':
                image_status = i[1]
            if i[0] == 'image_uris':
                image_uris = i[1]
            if i[0] == 'mana_cost':
                mana_cost = i[1]
            if i[0] == 'cmc':
                cmc = i[1]
            if i[0] == 'type_line':
                type_line = i[1]
            if i[0] == 'oracle_text':
                oracle_text = i[1]
            if i[0] == 'power':
                power = i[1]
            if i[0] == 'toughness':
                toughness = i[1]
            if i[0] == 'colors':
                colors = i[1]
            if i[0] == 'color_identity':
                color_identity = i[1]
            if i[0] == 'keywords':
                keywords = i[1]
            if i[0] == 'all_parts':
                all_parts = i[1]
            if i[0] == 'legalities':
                legalities = i[1]
            if i[0] == 'games':
                games = i[1]
            if i[0] == 'reserved':
                reserved = i[1]
            if i[0] == 'foil':
                foil = i[1]
            if i[0] == 'nonfoil':
                nonfoil = i[1]
            if i[0] == 'finishes':
                finishes = i[1]
            if i[0] == 'oversized':
                oversized = i[1]
            if i[0] == 'promo':
                promo = i[1]
            if i[0] == 'reprint':
                reprint = i[1]
            if i[0] == 'variation':
                variation = i[1]
            if i[0] == 'set_id':
                set_id = i[1]
            if i[0] == 'set':
                sets = i[1]
            if i[0] == 'set_name':
                set_name = i[1]
            if i[0] == 'set_type':
                set_type = i[1]
            if i[0] == 'set_uri':
                set_uri = i[1]
            if i[0] == 'set_search_uri':
                set_search_uri = i[1]
            if i[0] == 'scryfall_set_uri':
                scryfall_set_uri = i[1]
            if i[0] == 'rulings_uri':
                rulings_uri = i[1]
            if i[0] == 'prints_search_uri':
                prints_search_uri = i[1]
            if i[0] == 'collector_number':
                collector_number = i[1]
            if i[0] == 'digital':
                digital = i[1]
            if i[0] == 'rarity':
                rarity = i[1]
            if i[0] == 'watermark':
                watermark = i[1]
            if i[0] == 'flavor_text':
                flavor_text = i[1]
            if i[0] == 'card_back_id':
                card_back_id = i[1]
            if i[0] == 'artist':
                artist = i[1]
            if i[0] == 'artist_ids':
                artist_ids = i[1]
            if i[0] == 'illustration_id':
                illustration_id = i[1]
            if i[0] == 'border_color':
                border_color = i[1]
            if i[0] == 'frame':
                frame = i[1]
            if i[0] == 'security_stamp':
                security_stamp = i[1]
            if i[0] == 'full_art':
                full_art = i[1]
            if i[0] == 'textless':
                textless = i[1]
            if i[0] == 'booster':
                booster = i[1]
            if i[0] == 'story_spotlight':
                story_spotlight = i[1]
            if i[0] == 'edhrec_rank':
                edhrec_rank = i[1]
            if i[0] == 'prices':
                prices = i[1]
            if i[0] == 'related_uris':
                related_uris = i[1]
            if i[0] == 'purchase_uris':
                purchase_uris = i[1]
        # check existing record in database if recod is not available then insert
        kwargs = {'id': ids}
        where_clause = 'WHERE ' + ' AND '.join([' ' + k + ' = %s' for k in kwargs.keys()])
        values = tuple(kwargs.values())
        sql = "SELECT ID FROM scryfalls " + where_clause
        cursor.execute(sql, values)
        results = cursor.fetchone()
        if str(results) == 'None' or str(results) == None:
            data = {'object': str(objects) ,'id':str(ids),'oracle_id':str(oracle_id),'multiverse_ids': str(multiverse_ids),'mtgo_id':str(mtgo_id),'mtgo_foil_id':str(mtgo_foil_id), 'tcgplayer_id':str(tcgplayer_id),'cardmarket_id':str(cardmarket_id),'name':str(name),'lang':str(lang), 'released_at':str(released_at),'uri':str(uri),'scryfall_uri':str(scryfall_uri),'layout':str(layout), 'highres_image':str(highres_image),'image_status':str(image_status),'image_uris':str(image_uris),'mana_cost':str(mana_cost),'cmc':str(cmc), 'type_line':str(type_line),'oracle_text':str(oracle_text),'power':str(power),'toughness':str(toughness), 'colors':str(colors),'color_identity':str(color_identity),'keywords':str(keywords),'all_parts':str(all_parts),'legalities':str(legalities),'games':str(games), 'reserved':str(reserved),'foil':str(foil),'nonfoil':str(nonfoil),'finishes':str(finishes), 'oversized':str(oversized),'promo':str(promo),'reprint':str(reprint),'variation':str(variation),'set_id':str(set_id),'sets':str(sets), 'set_name':str(set_name),'set_type':str(set_type),'set_uri':str(set_uri),'set_search_uri':str(set_search_uri), 'scryfall_set_uri':str(scryfall_set_uri),'rulings_uri':str(rulings_uri),'prints_search_uri':str(prints_search_uri),'collector_number':str(collector_number),'digital':str(digital), 'rarity':str(rarity),'watermark':str(watermark),'flavor_text':str(flavor_text),'card_back_id':str(card_back_id), 'artist':str(artist),'artist_ids':str(artist_ids),'illustration_id':str(illustration_id),'border_color':str(border_color),'frame':str(frame), 'full_art':str(full_art),'textless':str(textless),'booster':str(booster),'story_spotlight':str(story_spotlight), 'edhrec_rank':str(edhrec_rank) ,'prices':str(prices) ,'related_uris': str(related_uris) ,'purchase_uris':str(purchase_uris)}
            sql="""INSERT INTO scryfalls (object,id, oracle_id,multiverse_ids ,mtgo_id,mtgo_foil_id, tcgplayer_id,cardmarket_id,name,lang, released_at,uri,scryfall_uri,layout, highres_image,image_status,image_uris,mana_cost,cmc, type_line,oracle_text,power,toughness, colors,color_identity,keywords,all_parts,legalities,games, reserved,foil,nonfoil,finishes, oversized,promo,reprint,variation,set_id,sets, set_name,set_type,set_uri,set_search_uri, scryfall_set_uri,rulings_uri,prints_search_uri,collector_number,digital, rarity,watermark,flavor_text,card_back_id, artist,artist_ids,illustration_id,border_color,frame, full_art,textless,booster,story_spotlight, edhrec_rank ,prices ,related_uris ,purchase_uris) VALUES {}""".format(tuple(data.values()))
            cursor.execute(sql)
            mydb.commit()
            print('************************************Insert new Record****************************************')
        else:
            print("Id exist:-------------------",results[0])
if __name__ == '__main__':
    # call main function
    Scryfall()
    


# In[31]:


import requests,json,time
Api = requests.get('https://api.scryfall.com/cards/named?fuzzy=A-Cosmos Elixir')
Api_data = Api.json()


# In[ ]:


try:
       if results == results[0]:
           print("Id exist:-------------------",results)
           print('\r')
       elif str(results) == None or str(results) == "None": 
           print('************************************Insert new Record****************************************')
           data = {'object': str(objects) ,'id':str(ids),'oracle_id':str(oracle_id),'multiverse_ids': str(multiverse_ids),'mtgo_id':str(mtgo_id),'mtgo_foil_id':str(mtgo_foil_id), 'tcgplayer_id':str(tcgplayer_id),'cardmarket_id':str(cardmarket_id),'name':str(name),'lang':str(lang), 'released_at':str(released_at),'uri':str(uri),'scryfall_uri':str(scryfall_uri),'layout':str(layout), 'highres_image':str(highres_image),'image_status':str(image_status),'image_uris':str(image_uris),'mana_cost':str(mana_cost),'cmc':str(cmc), 'type_line':str(type_line),'oracle_text':str(oracle_text),'power':str(power),'toughness':str(toughness), 'colors':str(colors),'color_identity':str(color_identity),'keywords':str(keywords),'all_parts':str(all_parts),'legalities':str(legalities),'games':str(games), 'reserved':str(reserved),'foil':str(foil),'nonfoil':str(nonfoil),'finishes':str(finishes), 'oversized':str(oversized),'promo':str(promo),'reprint':str(reprint),'variation':str(variation),'set_id':str(set_id),'sets':str(sets), 'set_name':str(set_name),'set_type':str(set_type),'set_uri':str(set_uri),'set_search_uri':str(set_search_uri), 'scryfall_set_uri':str(scryfall_set_uri),'rulings_uri':str(rulings_uri),'prints_search_uri':str(prints_search_uri),'collector_number':str(collector_number),'digital':str(digital), 'rarity':str(rarity),'watermark':str(watermark),'flavor_text':str(flavor_text),'card_back_id':str(card_back_id), 'artist':str(artist),'artist_ids':str(artist_ids),'illustration_id':str(illustration_id),'border_color':str(border_color),'frame':str(frame), 'full_art':str(full_art),'textless':str(textless),'booster':str(booster),'story_spotlight':str(story_spotlight), 'edhrec_rank':str(edhrec_rank) ,'prices':str(prices) ,'related_uris': str(related_uris) ,'purchase_uris':str(purchase_uris)}
           sql="""INSERT INTO scryfalls (object,id, oracle_id,multiverse_ids ,mtgo_id,mtgo_foil_id, tcgplayer_id,cardmarket_id,name,lang, released_at,uri,scryfall_uri,layout, highres_image,image_status,image_uris,mana_cost,cmc, type_line,oracle_text,power,toughness, colors,color_identity,keywords,all_parts,legalities,games, reserved,foil,nonfoil,finishes, oversized,promo,reprint,variation,set_id,sets, set_name,set_type,set_uri,set_search_uri, scryfall_set_uri,rulings_uri,prints_search_uri,collector_number,digital, rarity,watermark,flavor_text,card_back_id, artist,artist_ids,illustration_id,border_color,frame, full_art,textless,booster,story_spotlight, edhrec_rank ,prices ,related_uris ,purchase_uris) VALUES {}""".format(tuple(data.values()))
           cursor.execute(sql)
           mydb.commit()
   except:
       print("////")


# In[ ]:





# In[256]:


kwargs = {'id': '4945031e-1158-474c-9e50-1ec817acc767'}
where_clause = 'WHERE ' + ' AND '.join([' ' + k + ' = %s' for k in kwargs.keys()])
values = tuple(kwargs.values())
sql = "SELECT ID FROM scryfalls " + where_clause
cursor.execute(sql, values)
results = cursor.fetchone()


# In[257]:


results


# In[235]:


results[0]


# In[9]:


object = ''
id = ''
oracle_id = ''
multiverse_ids = ''
name = ''
lang = ''
released_at = ''
uri= ''
scryfall_uri= ''
layout= ''
highres_image= ''
image_status = ''
image_uris = ''
mana_cost = ''
cmc = ''
type_line = ''
oracle_text = ''
colors = ''
color_identity = ''
keywords = ''
all_parts = ''
legalities = ''
games = ''
reserved = ''
foil = ''
nonfoil = ''
finishes = ''
oversized = ''
promo = ''
reprint = ''
variation = ''
set_id = ''
set = ''
set_name = ''
set_type = ''
set_uri = ''
set_search_uri = ''
scryfall_set_uri = ''
rulings_uri = ''
prints_search_uri = ''
collector_number = ''
digital = ''
rarity = ''
card_back_id = ''
artist = ''
artist_ids = ''
illustration_id = ''
border_color = ''
frame = ''
security_stamp = ''
full_art = ''
textless = ''
booster = ''
story_spotlight = ''
prices = ''
related_uris = ''


# In[36]:


for i in list:
    print(i[0],'                           ',i[1])


# In[ ]:





# In[13]:


objects = ''
ids = ''
oracle_id = ''
stroracle_id = ''
mtgo_id = ''
multiverse_ids = ''
name = ''
lang = ''
released_at = ''
uri= ''
scryfall_uri= ''
layout= ''
highres_image= ''
image_status = ''
image_uris = ''
mana_cost = ''
cmc = ''
type_line = ''
oracle_text = ''
colors = ''
color_identity = ''
keywords = ''
all_parts = ''
legalities = ''
games = ''
reserved = ''
foil = ''
nonfoil = ''
finishes = ''
oversized = ''
promo = ''
reprint = ''
variation = ''
set_id = ''
sets = ''
set_name = ''
set_type = ''
set_uri = ''
set_search_uri = ''
scryfall_set_uri = ''
rulings_uri = ''
prints_search_uri = ''
collector_number = ''
digital = ''
rarity = ''
card_back_id = ''
artist = ''
artist_ids = ''
illustration_id = ''
border_color = ''
frame = ''
security_stamp = ''
full_art = ''
textless = ''
booster = ''
story_spotlight = ''
prices = ''
related_uris = ''
mtgo_foil_id =''
tcgplayer_id=''
cardmarket_id=''
power=''
toughness=''
watermark=''
flavor_text=''
edhrec_rank=''
purchase_uris = ''
for i in list:
#     print(i[0])
    if i[0] == 'object':
        objects = i[1]  
        print(objects)
    if i[0] == 'id':
        ids = i[1]
        print(ids)
    if i[0] == 'stroracle_id':
        stroracle_id = i[1]
    
    if  i[0] == 'oracle_id':
        oracle_id = i[1]
        print(oracle_id)
    if i[0] == 'multiverse_ids':
        multiverse_ids = i[1]
        print(multiverse_ids)
    if i[0] == 'mtgo_id':
        mtgo_id = i[1]
        print(mtgo_id)
    if i[0] =='mtgo_foil_id': 
        mtgo_foil_id = i[1]
        print(mtgo_foil_id)
    if i[0] == 'tcgplayer_id':
        tcgplayer_id = i[1]
        print(tcgplayer_id)
    if i[0] == 'cardmarket_id':
        cardmarket_id = i[1]
        print(cardmarket_id)
    if i[0] == 'name':
        name = i[1]
        print(name)
    if i[0] == 'lang':
        lang = i[1]
        print(lang)
    if i[0] == 'released_at':
        released_at = i[1]
        print(released_at)
    if i[0] == 'uri':
        uri = i[1]
        print(uri)
    if i[0] == 'scryfall_uri':
        scryfall_uri = i[1]
        print(scryfall_uri)
    if i[0] == 'layout':
        layout = i[1]
        print(layout)
    if i[0] == 'highres_image':
        highres_image = i[1]
        print(highres_image)
    if i[0] == 'image_status':
        image_status = i[1]
        print(image_status)
    if i[0] == 'image_uris':
        image_uris = i[1]
        print(image_uris)
    if i[0] == 'mana_cost':
        mana_cost = i[1]
        print(mana_cost)
    if i[0] == 'cmc':
        cmc = i[1]
        print(cmc)
    if i[0] == 'type_line':
        type_line = i[1]
        print(type_line)
    if i[0] == 'oracle_text':
        oracle_text = i[1]
        print(oracle_text)
    if i[0] == 'power':
        power = i[1]
        print(power)
    if i[0] == 'toughness':
        toughness = i[1]
        print(toughness)
    if i[0] == 'colors':
        colors = i[1]
        print(colors)
    if i[0] == 'color_identity':
        color_identity = i[1]
        print(color_identity)
    if i[0] == 'keywords':
        keywords = i[1]
        print(keywords)
    if i[0] == 'all_parts':
        all_parts = i[1]
        print(all_parts)
    if i[0] == 'legalities':
        legalities = i[1]
        print(legalities)
    if i[0] == 'games':
        games = i[1]
        print(games)
    if i[0] == 'reserved':
        reserved = i[1]
        print(reserved)
    if i[0] == 'foil':
        foil = i[1]
        print(foil)
    if i[0] == 'nonfoil':
        nonfoil = i[1]
        print(nonfoil)
    if i[0] == 'finishes':
        finishes = i[1]
        print(finishes)
    if i[0] == 'oversized':
        oversized = i[1]
        print(oversized)
    if i[0] == 'promo':
        promo = i[1]
        print(promo)
    if i[0] == 'reprint':
        reprint = i[1]
        print(reprint)
    if i[0] == 'variation':
        variation = i[1]
        print(variation)
    if i[0] == 'set_id':
        set_id = i[1]
        print(set_id)
    if i[0] == 'set':
        sets = i[1]
        print(sets)
    if i[0] == 'set_name':
        set_name = i[1]
        print(set_name)
    if i[0] == 'set_type':
        set_type = i[1]
        print(set_type)
    if i[0] == 'set_uri':
        set_uri = i[1]
        print(set_uri)
    if i[0] == 'set_search_uri':
        set_search_uri = i[1]
        print(set_search_uri)
    if i[0] == 'scryfall_set_uri':
        scryfall_set_uri = i[1]
        print(scryfall_set_uri)
    if i[0] == 'rulings_uri':
        rulings_uri = i[1]
        print(rulings_uri)
    if i[0] == 'prints_search_uri':
        prints_search_uri = i[1]
        print(prints_search_uri)
    if i[0] == 'collector_number':
        collector_number = i[1]
        print(collector_number)
    if i[0] == 'digital':
        digital = i[1]
        print(digital)
    if i[0] == 'rarity':
        rarity = i[1]
        print(rarity)
    if i[0] == 'watermark':
        watermark = i[1]
        print(watermark)
    if i[0] == 'flavor_text':
        flavor_text = i[1]
        print(flavor_text)
    if i[0] == 'card_back_id':
        card_back_id = i[1]
        print(card_back_id)
    if i[0] == 'artist':
        artist = i[1]
        print(artist)
    if i[0] == 'artist_ids':
        artist_ids = i[1]
        print(artist_ids)
    if i[0] == 'illustration_id':
        illustration_id = i[1]
        print(illustration_id)
    if i[0] == 'border_color':
        border_color = i[1]
        print(border_color)
    if i[0] == 'frame':
        frame = i[1]
        print(frame)
    if i[0] == 'security_stamp':
        security_stamp = i[1]
        print(security_stamp)
    if i[0] == 'full_art':
        full_art = i[1]
        print(full_art)
    if i[0] == 'textless':
        textless = i[1]
        print(textless)
    if i[0] == 'booster':
        booster = i[1]
        print(booster)
    if i[0] == 'story_spotlight':
        story_spotlight = i[1]
        print(story_spotlight)
    if i[0] == 'edhrec_rank':
        edhrec_rank = i[1]
        print(edhrec_rank)
    if i[0] == 'prices':
        prices = i[1]
        print(prices)
    if i[0] == 'related_uris':
        related_uris = i[1]
        print(related_uris)
    if i[0] == 'purchase_uris':
        purchase_uris = i[1]
data = {'object': objects ,'id':ids,'oracle_id':oracle_id,'multiverse_ids': str(multiverse_ids),'mtgo_id':mtgo_id,'mtgo_foil_id':mtgo_foil_id, 'tcgplayer_id':tcgplayer_id,'cardmarket_id':cardmarket_id,'name':name,'lang':lang, 'released_at':released_at,'uri':uri,'scryfall_uri':scryfall_uri,'layout':layout, 'highres_image':highres_image,'image_status':image_status,'image_uris':str(image_uris),'mana_cost':mana_cost,'cmc':cmc, 'type_line':type_line,'oracle_text':oracle_text,'power':power,'toughness':toughness, 'colors':str(colors),'color_identity':str(color_identity),'keywords':str(keywords),'all_parts':str(all_parts),'legalities':str(legalities),'games':str(games), 'reserved':reserved,'foil':foil,'nonfoil':nonfoil,'finishes':str(finishes), 'oversized':oversized,'promo':promo,'reprint':reprint,'variation':variation,'set_id':set_id,'sets':sets, 'set_name':set_name,'set_type':set_type,'set_uri':set_uri,'set_search_uri':set_search_uri, 'scryfall_set_uri':scryfall_set_uri,'rulings_uri':rulings_uri,'prints_search_uri':prints_search_uri,'collector_number':collector_number,'digital':digital, 'rarity':rarity,'watermark':watermark,'flavor_text':flavor_text,'card_back_id':card_back_id, 'artist':artist,'artist_ids':str(artist_ids),'illustration_id':illustration_id,'border_color':border_color,'frame':frame, 'full_art':full_art,'textless':textless,'booster':booster,'story_spotlight':story_spotlight, 'edhrec_rank':edhrec_rank ,'prices':str(prices) ,'related_uris':str(related_uris) ,'purchase_uris':purchase_uris}
#     print(data)
sql="""INSERT INTO scryfalls (object,id, oracle_id,multiverse_ids ,mtgo_id,mtgo_foil_id, tcgplayer_id,cardmarket_id,name,lang, released_at,uri,scryfall_uri,layout, highres_image,image_status,image_uris,mana_cost,cmc, type_line,oracle_text,power,toughness, colors,color_identity,keywords,all_parts,legalities,games, reserved,foil,nonfoil,finishes, oversized,promo,reprint,variation,set_id,sets, set_name,set_type,set_uri,set_search_uri, scryfall_set_uri,rulings_uri,prints_search_uri,collector_number,digital, rarity,watermark,flavor_text,card_back_id, artist,artist_ids,illustration_id,border_color,frame, full_art,textless,booster,story_spotlight, edhrec_rank ,prices ,related_uris ,purchase_uris) VALUES {}""".format(tuple(data.values()))
cursor.execute(sql)
mydb.commit()


# In[ ]:


image_uris = []
legalities = []
prices = []
related_uris = []
purchase_uris = []
all_parts=[]
for i in list:
#     print(i[0])
    if 'object' in i[0]:
        object = i[1]  
        print(object)
    if 'id' in i[0]:
        id = i[1]
        print(id)
#     if 'stroracle_id' in i[0]:
#         stroracle_id = i[1]
#         print(stroracle_id)
#     if 'oracle_id' in i[0]:
#         oracle_id = i[1]
#         print(oracle_id)
#     if 'multiverse_ids' in i[0]:
#         multiverse_ids = i[1]
#         print(multiverse_ids)
#     if 'mtgo_id' in i[0]:
#         mtgo_id = i[1]
#         print(mtgo_id)
#     if 'mtgo_foil_id' in i[0]:
#         mtgo_foil_id = i[1]
#         print(mtgo_foil_id)
#     if 'tcgplayer_id' in i[0]:
#         tcgplayer_id = i[1]
#         print(tcgplayer_id)
#     if 'cardmarket_id' in i[0]:
#         cardmarket_id = i[1]
#         print(cardmarket_id)
#     if 'name' in i[0]:
#         name = i[1]
#         print(name)
#     if 'lang' in i[0]:
#         lang = i[1]
#         print(lang)
#     if 'released_at' in i[0]:
#         released_at = i[1]
#         print(released_at)
#     if 'uri' in i[0]:
#         uri = i[1]
#         print(uri)
#     if 'scryfall_uri' in i[0]:
#         scryfall_uri = i[1]
#         print(scryfall_uri)
#     if 'layout' in i[0]:
#         layout = i[1]
#         print(layout)
#     if 'highres_image' in i[0]:
#         highres_image = i[1]
#         print(highres_image)
#     if 'image_status' in i[0]:
#         image_status = i[1]
#         print(image_status)
#     if 'image_uris' in i[0]:
#         image_uris = i[1]
#         print(image_uris)
#     if 'mana_cost' in i[0]:
#         mana_cost = i[1]
#         print(mana_cost)
#     if 'cmc' in i[0]:
#         cmc = i[1]
#         print(cmc)
#     if 'type_line' in i[0]:
#         type_line = i[1]
#         print(type_line)
#     if 'oracle_text' in i[0]:
#         oracle_text = i[1]
#         print(oracle_text)
#     if 'power' in i[0]:
#         power = i[1]
#         print(power)
#     if 'toughness' in i[0]:
#         toughness = i[1]
#         print(toughness)
#     if 'colors' in i[0]:
#         colors = i[1]
#         print(colors)
#     if 'color_identity' in i[0]:
#         color_identity = i[1]
#         print(color_identity)
#     if 'keywords' in i[0]:
#         keywords = i[1]
#         print(keywords)
#     if 'all_parts' in i[0]:
#         all_parts = i[1]
#         print(all_parts)
#     if 'legalities' in i[0]:
#         legalities = i[1]
#         print(legalities)
#     if 'games' in i[0]:
#         games = i[1]
#         print(games)
#     if 'reserved' in i[0]:
#         reserved = i[1]
#         print(reserved)
#     if 'foil' in i[0]:
#         foil = i[1]
#         print(foil)
#     if 'nonfoil' in i[0]:
#         nonfoil = i[1]
#         print(nonfoil)
#     if 'finishes' in i[0]:
#         finishes = i[1]
#         print(finishes)
#     if 'oversized' in i[0]:
#         oversized = i[1]
#         print(oversized)
#     if 'promo' in i[0]:
#         promo = i[1]
#         print(promo)
#     if 'reprint' in i[0]:
#         reprint = i[1]
#         print(reprint)
#     if 'variation' in i[0]:
#         variation = i[1]
#         print(variation)
#     if 'set_id' in i[0]:
#         set_id = i[1]
#         print(set_id)
#     if 'set' in i[0]:
#         set = i[1]
#         print(set)
#     if 'set_name' in i[0]:
#         set_name = i[1]
#         print(set_name)
#     if 'set_type' in i[0]:
#         set_type = i[1]
#         print(set_type)
#     if 'set_uri' in i[0]:
#         set_uri = i[1]
#         print(set_uri)
#     if 'set_search_uri' in i[0]:
#         set_search_uri = i[1]
#         print(set_search_uri)
#     if 'scryfall_set_uri' in i[0]:
#         scryfall_set_uri = i[1]
#         print(scryfall_set_uri)
#     if 'rulings_uri' in i[0]:
#         rulings_uri = i[1]
#         print(rulings_uri)
#     if 'prints_search_uri' in i[0]:
#         prints_search_uri = i[1]
#         print(prints_search_uri)
#     if 'collector_number' in i[0]:
#         collector_number = i[1]
#         print(collector_number)
#     if 'digital' in i[0]:
#         digital = i[1]
#         print(digital)
#     if 'rarity' in i[0]:
#         rarity = i[1]
#         print(rarity)
#     if 'watermark' in i[0]:
#         watermark = i[1]
#         print(watermark)
#     if 'flavor_text' in i[0]:
#         flavor_text = i[1]
#         print(flavor_text)
#     if 'card_back_id' in i[0]:
#         card_back_id = i[1]
#         print(card_back_id)
#     if 'artist' in i[0]:
#         artist = i[1]
#         print(artist)
#     if 'artist_ids' in i[0]:
#         artist_ids = i[1]
#         print(artist_ids)
#     if 'illustration_id' in i[0]:
#         illustration_id = i[1]
#         print(illustration_id)
#     if 'border_color' in i[0]:
#         border_color = i[1]
#         print(border_color)
#     if 'frame' in i[0]:
#         frame = i[1]
#         print(frame)
#     if 'security_stamp' in i[0]:
#         security_stamp = i[1]
#         print(security_stamp)
#     if 'full_art' in i[0]:
#         full_art = i[1]
#         print(full_art)
#     if 'textless' in i[0]:
#         textless = i[1]
#         print(textless)
#     if 'booster' in i[0]:
#         booster = i[1]
#         print(booster)
#     if 'story_spotlight' in i[0]:
#         story_spotlight = i[1]
#         print(story_spotlight)
#     if 'edhrec_rank' in i[0]:
#         edhrec_rank = i[1]
#         print(edhrec_rank)
#     if 'prices' in i[0]:
#         prices = i[1]
#         print(prices)
#     if 'related_uris' in i[0]:
#         related_uris = i[1]
#         print(related_uris)
#     sql="insert into news_feed(object,id, oracle_id,multiverse_ids ,mtgo_id,mtgo_foil_id, tcgplayer_id,cardmarket_id,name,lang, released_at,uri,scryfall_uri,layout, highres_image,image_status,image_uris,mana_cost,cmc, type_line,oracle_text,power,toughness, colors,color_identity,keywords,all_parts,legalities,games, reserved,foil,nonfoil,finishes, oversized,promo,reprint,variation,set_id,sets, set_name,set_type,set_uri,set_search_uri, scryfall_set_uri,rulings_uri,prints_search_uri,collector_number,digital, rarity,watermark,flavor_text,card_back_id, artist,artist_ids,illustration_id,border_color,frame, full_art,textless,booster,story_spotlight, edhrec_rank ,prices ,related_uris ,purchase_uris ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
#     value=(object,id, stroracle_id,str(multiverse_ids) ,mtgo_id,mtgo_foil_id, tcgplayer_id,cardmarket_id,name,lang, released_at,uri,scryfall_uri,layout, highres_image,image_status,image_uris,mana_cost,cmc, type_line,oracle_text,power,toughness, str(colors),str(color_identity),str(keywords),all_parts,legalities,str(games), reserved,foil,nonfoil,str(finishes), oversized,promo,reprint,variation,set_id,set, set_name,set_type,set_uri,set_search_uri, scryfall_set_uri,rulings_uri,prints_search_uri,collector_number,digital, rarity,watermark,flavor_text,card_back_id, artist,str(artist_ids),illustration_id,border_color,frame, full_art,textless,booster,story_spotlight, edhrec_rank ,prices ,related_uris ,purchase_uris)
#     obj.execute(sql,str(value))
#     mydb.commit()
# #     try:
#         print(i[1]['small'])
#         image_uris.append(i[1]['small'])
#         image_uris.append(i[1]['normal'])
#         image_uris.append(i[1]['large'],)
#         image_uris.append(i[1]['png'],)
#         image_uris.append(i[1]['art_crop'],)
#         image_uris.append(i[1]['border_crop'],)
#     except:
#         pass
#     try:
#         legalities.append(i[1]['standard'])
#         legalities.append(i[1]['future'])
#         legalities.append(i[1]['historic'],)
#         legalities.append(i[1]['gladiator'],)
#         legalities.append(i[1]['pioneer'],)
#         legalities.append(i[1]['modern'],)
#         legalities.append(i[1]['legacy'])
#         legalities.append(i[1]['pauper'])
#         legalities.append(i[1]['vintage'],)
#         legalities.append(i[1]['penny'],)
#         legalities.append(i[1]['commander'],)
#         legalities.append(i[1]['brawl'],)
#         legalities.append(i[1]['legacy'])
#         legalities.append(i[1]['historicbrawl'])
#         legalities.append(i[1]['alchemy'],)
#         legalities.append(i[1]['paupercommander'],)
#         legalities.append(i[1]['duel'],)
#         legalities.append(i[1]['oldschool'],)
#         legalities.append(i[1]['premodern'],)

#     except:
#         pass
#     try:
#         prices.append(i[1]['usd'])
#         prices.append(i[1]['usd_foil'])
#         prices.append(i[1]['usd_etched'],)
#         prices.append(i[1]['eur'],)
#         prices.append(i[1]['eur_foil'],)
#         prices.append(i[1]['tix'],)
#     except:
#         pass
#     try:
#         related_uris.append(i[1]['gatherer'])
#         related_uris.append(i[1]['tcgplayer_infinite_articles'])
#         related_uris.append(i[1]['tcgplayer_infinite_decks'],)
#         related_uris.append(i[1]['edhrec'],)
#         related_uris.append(i[1]['mtgtop8'],)
#     except:
#         pass
#     try:
#         purchase_uris.append(i[1]['tcgplayer'])
#         purchase_uris.append(i[1]['cardmarket'])
#         purchase_uris.append(i[1]['cardhoarder'],)
#     except:
#         pass
#     try:
#         all_parts.append(i[1]['object'])
#         all_parts.append(i[1]['id'])
#         all_parts.append(i[1]['component'],)
#         all_parts.append(i[1]['name'],)
#         all_parts.append(i[1]['type_line'],)
#         all_parts.append(i[1]['uri'],)
#     except:
#         pass
    


# In[15]:


artist,artist_ids


# In[52]:


len(i[0])


# In[49]:


sql="insert into news_feed(object,id, oracle_id,multiverse_ids ,mtgo_id,mtgo_foil_id, tcgplayer_id,cardmarket_id,name,lang, released_at,uri,scryfall_uri,layout, highres_image,image_status,image_uris,mana_cost,cmc, type_line,oracle_text,power,toughness, colors,color_identity,keywords,all_parts,legalities,games, reserved,foil,nonfoil,finishes, oversized,promo,reprint,variation,set_id,sets, set_name,set_type,set_uri,set_search_uri, scryfall_set_uri,rulings_uri,prints_search_uri,collector_number,digital, rarity,watermark,flavor_text,card_back_id, artist,artist_ids,illustration_id,border_color,frame, full_art,textless,booster,story_spotlight, edhrec_rank ,prices ,related_uris ,purchase_uris ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
value = (str(object),str(id),str(oracle_id),str(multiverse_ids) ,str(mtgo_id),str(mtgo_foil_id), str(tcgplayer_id),str(cardmarket_id),str(name,lang), str(released_at),str(uri,scryfall_uri),str(layout), str(highres_image),str(image_status),str(image_uris),str(mana_cost,cmc), str(type_line),str(oracle_text),str(power),str(toughness), str(colors),str(color_identity),str(keywords),str(all_parts),str(legalities),str(games), str(reserved),str(foil),str(nonfoil),str(finishes), str(oversized),str(promo),str(reprint),str(variation),str(set_id),str(set), str(set_name),str(set_type),str(set_uri),str(set_search_uri), str(scryfall_set_uri),str(rulings_uri),str(prints_search_uri),str(collector_number),str(digital), str(rarity),str(watermark),str(flavor_text),str(card_back_id), str(artist),str(artist_ids),str(illustration_id),str(border_color),str(frame), str(full_art),str(textless),str(booster),str(story_spotlight), str(edhrec_rank) ,str(prices ,str(related_uris) ,str(purchase_uris)))
print(type(value))


# In[35]:


list


# In[58]:





# In[241]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='scryfall_apis'
)
cursor = mydb.cursor(buffered=True)


# In[127]:


data = {'object':,'Ids':'93bec3c0-0260-4d31-8064-5d01efb4153f'}
print(data)
sql="""INSERT INTO jass (object,id, oracle_id,multiverse_ids ,mtgo_id,mtgo_foil_id, tcgplayer_id,cardmarket_id,name,lang, released_at,uri,scryfall_uri,layout, highres_image,image_status,image_uris,mana_cost,cmc, type_line,oracle_text,power,toughness, colors,color_identity,keywords,all_parts,legalities,games, reserved,foil,nonfoil,finishes, oversized,promo,reprint,variation,set_id,sets, set_name,set_type,set_uri,set_search_uri, scryfall_set_uri,rulings_uri,prints_search_uri,collector_number,digital, rarity,watermark,flavor_text,card_back_id, artist,artist_ids,illustration_id,border_color,frame, full_art,textless,booster,story_spotlight, edhrec_rank ,prices ,related_uris ,purchase_uris) VALUES {}""".format(tuple(data.values()))
cursor.execute(sql)
mydb.commit()


# In[128]:





# In[ ]:




