# from asyncio.windows_events import NULL
import mysql.connector, urllib.request, time, json, ssl, random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, jsonify, send_from_directory, request
from scrapper import get_data_hashtag, get_data_post
from mailer import send
from datetime import datetime


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="instalyze"
)

app = Flask('__name__')

@app.post('/register')
def register():
    mycursor    = mydb.cursor()
    email       = request.json['email']
    username    = request.json['username']
    name        = request.json['name']
    password    = request.json['password']
    response    = []
    
    # ===== DATASET IS EXISTS
    sql = """
        SELECT * FROM user
        WHERE USERNAME_USER = '"""+username+"""'
    """
    mycursor.execute(sql)
    result = mycursor.fetchone()

    
    if result != None:
        res = {}
        res['stat'] = "0"
        res['msg']  = 'Username alredy exists'
        response.append(res)

        return jsonify(response)
    
    sql = """
            INSERT INTO user (USERNAME_USER, NAME_USER, PASSWORD_USER, EMAIL_USER) VALUES (%s, %s, %s, %s)
        """ 
    values = (username, name, password, email)
    mycursor.execute(sql, values)
    mydb.commit()

    res = {}
    res['stat'] = "1"
    res['msg']  = 'Successfully Register'
    response.append(res)
    return jsonify(response)

@app.post('/login')
def login():
    mycursor    = mydb.cursor()
    username    = request.json['username']
    password    = request.json['password']
    response    = []
    
    # ===== DATASET IS EXISTS
    sql = """
        SELECT * FROM user
        WHERE USERNAME_USER = '"""+username+"""' AND PASSWORD_USER = '"""+password+"""'
    """
    mycursor.execute(sql)
    result = mycursor.fetchone()

    
    if result == None:
        res = {}
        res['stat'] = "0"
        res['msg']  = 'Username or Password is wrong'
        response.append(res)

        return jsonify(response)
    

    res = {}
    res['stat'] = "1"
    res['msg']  = 'Successfully Login'

    res['data'] = {}
    res['data']['USERNAME_USER']    = result[0]
    res['data']['NAME_USER']        = result[1]
    res['data']['EMAIL_USER']       = result[3]
    
    response.append(res)
    return jsonify(response)

@app.route('/upload-profile/<path:filename>') 
def get_post_pic(filename): 
    return send_from_directory('img/profile/', filename)

@app.route('/upload-post/<path:filename>') 
def get_profile_pic(filename): 
    return send_from_directory('img/post/', filename)

@app.route('/upload-graph/<path:filename>') 
def get_graph_pic(filename): 
    return send_from_directory('graph/', filename)

@app.route('/user-dataset/<username>')
def user_dataset(username):
    mycursor = mydb.cursor()
    sql = """
            SELECT d.*
            FROM dataset d 
            WHERE d.USERNAME_USER = '"""+username+"""'
        """
    mycursor.execute(sql)

    results = mycursor.fetchall()
    datas   = []
    for result in results:
        temp = {}
        temp['HASHTAG_DATASET']         = result[0]
        temp['TOTPOST_DATASET']         = result[1]
        temp['TOTLIKE_DATASET']         = result[2]
        temp['TOTCOMMENT_DATASET']      = result[3]
        temp['created_at']              = result[4]
        temp['USERNAME_USER']           = result[5]
        temp['COLOR_DATASET']           = result[6]
        temp['IMGINFLUENCER_DATASET']   = result[7]
        temp['ID_DATASET']              = result[8]
        temp['ISACTIVE_DATASET']        = result[9]
        datas.append(temp)

    return jsonify(datas)

@app.route('/influencer/<id_dataset>')
def influencer(id_dataset):
    mycursor = mydb.cursor()
    sql = """
            SELECT *
            FROM influencer i 
            WHERE i.ID_DATASET = '"""+id_dataset+"""'
        """
    mycursor.execute(sql)

    results = mycursor.fetchall()
    datas   = []
    for result in results:
        temp = {}
        temp['ID_INFLUENCER']           = result[0]
        temp['ID_UD']                   = result[1]
        temp['USERNAME_INFLUENCER']     = result[2]
        temp['ACCURACY_INFLUENCER']     = result[3]
        datas.append(temp)

    return jsonify(datas)

@app.post('/user-setdataset')
def user_setdataset():
    mycursor    = mydb.cursor()
    hashtag     = request.json['hashtag']
    username    = request.json['username']
    id_dataset  = username+"""_"""+hashtag
    
    # ===== DATASET IS EXISTS
    sql = """
        SELECT * FROM dataset 
        WHERE ID_DATASET = '"""+id_dataset+"""'
    """
    mycursor.execute(sql)
    result = mycursor.fetchone()

    if result != None:
        user_deldataset(id_dataset)

    scrape(username, hashtag)
    detectInfluence(id_dataset)

    mydb.commit()
    return jsonify("success")

@app.post('/user-deldataset/<id_dataset>')
def user_deldataset(id_dataset):
    mycursor    = mydb.cursor()
    sql = """
        DELETE FROM dataset_detail 
        WHERE ID_DATASET = '"""+id_dataset+"""'
    """
    mycursor.execute(sql)
    
    sql = """
        DELETE FROM influencer 
        WHERE ID_DATASET = '"""+id_dataset+"""'
    """
    mycursor.execute(sql)

    sql = """
        DELETE FROM dataset 
        WHERE ID_DATASET = '"""+id_dataset+"""'
    """
    mycursor.execute(sql)

    mydb.commit()
    return jsonify("success")

@app.route("/posts/<id_dataset>")
def posts(id_dataset):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM dataset_detail WHERE ID_DATASET = '"+id_dataset+"' ORDER BY COUNTLIKE_DD DESC, COUNTCOMMENT_DD DESC"
    mycursor.execute(sql)

    results = mycursor.fetchall()
    datas = []
    for result in results:
        temp = {}
        temp['ID_DD']           = result[0]
        temp['SHORTCODE_DD']    = result[1]
        temp['USERNAME_DD']     = result[2]
        temp['DISPLAYURL_DD']   = result[3]
        temp['COUNTLIKE_DD']    = result[4]
        temp['COUNTCOMMENT_DD'] = result[5]
        temp['LISTTAGGED_DD']   = result[6]
        temp['PROFILEPICT_DD']  = result[7]
        temp['CAPTION_DD']      = result[8]
        temp['FULLNAME_DD']     = result[9]
        temp['created_at']      = result[10]
        temp['updated_at']      = result[11]
        temp['HASHTAG_DATASET'] = result[12]
        temp['TAKENAT_DD']      = result[13]
        temp['ID_DATASET']      = result[14]
        
        datas.append(temp)

    return jsonify(datas)

@app.route("/scrape/<username>/<hashtag>")
def scrape(username, hashtag):
    id_dataset      = username+"""_"""+hashtag
    dataset_hashtag = hashtag
    hashtag_scrapes = get_data_hashtag(dataset_hashtag)
    hashtag_scrapes = hashtag_scrapes['graphql']['hashtag']['edge_hashtag_to_media']['edges']
    list_data       = []

    x           = 1
    counter     = 0
    tot_like    = 0
    tot_post    = 0
    tot_comment = 0
    total_hashtag_scrape = len(hashtag_scrapes)
    print("Expected Total Data  : " + str(total_hashtag_scrape))

    while counter < total_hashtag_scrape:
        try:
            curr_date       = datetime.now()
            hashtag_scrape  = hashtag_scrapes[counter]['node']
            post_scrape     = get_data_post(hashtag_scrape['shortcode'])
            post_scrape     = post_scrape['items'][0]
            gcontext = ssl.SSLContext()

            r = urllib.request.urlopen(post_scrape['user']['profile_pic_url'], context=gcontext)
            profile_pic = "img/profile/"+hashtag_scrape['shortcode']
            with open("img/profile/"+hashtag_scrape['shortcode']+".jpg", "wb") as f:
                f.write(r.read())

            r = urllib.request.urlopen(hashtag_scrape['display_url'], context=gcontext)
            post_pic = "img/post/"+hashtag_scrape['shortcode']
            with open("img/post/"+hashtag_scrape['shortcode']+".jpg", "wb") as f:
                f.write(r.read())

            post = []
            post.append(id_dataset)
            post.append(dataset_hashtag) 
            post.append(hashtag_scrape['shortcode']) 
            post.append(post_scrape['user']['username']) 
            post.append(post_scrape['user']['full_name']) 
            post.append(profile_pic) 
            post.append(post_pic) 
            post.append(post_scrape['like_count'])
            post.append(post_scrape['comment_count']) 
            post.append(post_scrape['caption']['text']) 

            taken_at = post_scrape['taken_at']
            taken_at = datetime.fromtimestamp(taken_at)
            post.append(taken_at.strftime("%Y-%m-%d %H:%M:%S")) 
            post.append(curr_date.strftime("%Y-%m-%d %H:%M:%S")) 
            post.append(curr_date.strftime("%Y-%m-%d %H:%M:%S")) 

            try:
                list_tags = post_scrape['usertags']['in']
                tag_users = []
                
                for tag in list_tags:
                    tag_users.append(tag['user']['username'])
                post.append(';'.join(tag_users))
            except:
                post.append("")
            
            post = tuple(post)

            json.dumps(post)
            list_data.append(post)

            tot_like    = tot_like + int(post_scrape['like_count'])
            tot_comment = tot_comment + int(post_scrape['comment_count'])
            tot_post    = tot_post + 1

            print(x," | ",hashtag_scrape['shortcode'])
            time.sleep(1)            
            x = x + 1
        except: 
            time.sleep(3)

        # if counter == 5:
        #     break
        
        counter = counter + 1

    mycursor    = mydb.cursor()
    values      = ', '.join(map(str, list_data))

    sql = """
        INSERT INTO dataset (
            HASHTAG_DATASET, TOTPOST_DATASET, TOTLIKE_DATASET, 
            TOTCOMMENT_DATASET, created_at, USERNAME_USER, COLOR_DATASET,
            IMGINFLUENCER_DATASET, ID_DATASET
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    r = lambda: random.randint(0,255)
    color = '#%02X%02X%02X' % (r(),r(),r())

    graph_pic = "graph/"+id_dataset+".png"
    dataset = (dataset_hashtag, tot_post, tot_like, tot_comment, curr_date.strftime("%Y-%m-%d %H:%M:%S"), username, color, graph_pic, id_dataset)
    mycursor.execute(sql, dataset)

    mydb.commit()

    sql = """
        INSERT INTO 
            dataset_detail 
                (
                    ID_DATASET, HASHTAG_DATASET, SHORTCODE_DD, USERNAME_DD, 
                    FULLNAME_DD, PROFILEPICT_DD, DISPLAYURL_DD, 
                    COUNTLIKE_DD, COUNTCOMMENT_DD, CAPTION_DD, 
                    TAKENAT_DD, created_at, updated_at, LISTTAGGED_DD
                ) 
            VALUES {}
    """.format(values)
    
    mycursor.execute(sql)
    mydb.commit()

    
    return jsonify(list_data)

@app.route("/detect-influence/<id_dataset>")
def detectInfluence(id_dataset):
    mycursor = mydb.cursor()
    graph = nx.Graph()
    sql = """
        SELECT USERNAME_DD, LISTTAGGED_DD FROM dataset_detail WHERE ID_DATASET = '"""+id_dataset+"""' AND LISTTAGGED_DD != ""
    """
    mycursor.execute(sql)

    list_post = mycursor.fetchall()

    for list in list_post:
        tags = list[1].split(';')
        for tag in tags:
            graph.add_edge(list[0], tag)
    
    pos = nx.spring_layout(graph, k=0.2, iterations=20)
    plt.figure(figsize = (13, 7))
    nx.draw(graph, pos=pos)
    nx.draw_networkx_labels(graph, pos=pos)
    plt.savefig("graph/"+id_dataset+".png")
    # plt.show()

    most_influental = nx.degree_centrality(graph)
    list_data = []
    counter = 1
    for w in sorted(most_influental, key = most_influental.get, reverse = True):
        post = []
        post.append(id_dataset)
        post.append(w)
        post.append(round(most_influental[w],5))
        post = tuple(post)
        list_data.append(post)

        if counter == 10:
            break
        
        counter+=1
    
    values  = ', '.join(map(str, list_data))
    sql = """
        INSERT INTO 
            influencer
                (
                    ID_DATASET, USERNAME_INFLUENCER, ACCURACY_INFLUENCER
                ) 
            VALUES {}
    """.format(values)
    
    mycursor.execute(sql)
    mydb.commit()
    return most_influental

@app.route('/send-email')
def send_email():
    send()
    return "success"

if __name__ == "__main__":
    app.run(debug=True)