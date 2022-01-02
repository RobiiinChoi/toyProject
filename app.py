from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

#client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

#글작성 페이지
@app.route('/create')
def create_board():
    return render_template('create_board.html')

#메인페이지 글 리스트 출력
@app.route('/board')
def read_list():
    boards= list(db.board.find({},{'_id':False}).sort('regDate', -1))
    #boards = list(db.board.find({},{'_id':False}))
    return jsonify({'all_boards': boards})



# @app.route('/read_detail', methods=['GET'])
# def get_detail():
#     title_receive = request.form['title_give']
#     db.board.find_one({'title':title_receive},{'_id':False})
#     #boards = list(db.board.find({},{'_id':False}))
#     return jsonify({'msg':'솔팅 완료'})

# 글쓰기
@app.route('/write', methods=['POST'])
def write_board_detail():

    writer_receive = request.form['writer_give']
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    date_receive = request.form['date_give']
    review_number = 0;
    print(writer_receive)

    #current = datetime.datetime.now().date()
    #print(current)

    doc = {
        'writer': writer_receive,
        'title' : title_receive,
        'content' : content_receive,
        'regDate' : date_receive,
        'review' : review_number
    }
    db.board.insert_one(doc)

    return jsonify({'msg':'저장완료'})

@app.route('/read_detail', methods=['POST'])
def board_list():
    title_receive = request.form['title_give']
    db.board.find_one({'title':title_receive},{'_id':False})
    #boards = list(db.board.find({},{'_id':False}))
    return jsonify({'msg':'솔팅 완료'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)