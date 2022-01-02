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

# 메인페이지 글 리스트 출력
@app.route('/board')
def read_list():
    boards= list(db.board.find({},{'_id':False}).sort('regDate', -1))
    #boards = list(db.board.find({},{'_id':False}))
    return jsonify({'all_boards': boards})

# 상세 페이지
# @app.route('/detail_selected', methods=['GET'])
# def read_detail():
#     #board_one = db.board.find_one({'title': title_board_receive}, {'_id': False})
#     #boards = list(db.board.find({},{'_id':False}))
#     return jsonify({'board_one': board_one})

# 게시물 조회 수 증가
@app.route('/detail_selected', methods = ['POST'])
def view_up():
    title_board_receive = request.form['title_board_give']
    print(title_board_receive)
    db.board.update_one({'title':title_board_receive},{'$inc':{'review': 1}})
    #board_one = db.board.find_one({'title': title_board_receive}, {'_id': False})
    #boards = list(db.board.find({},{'_id':False}))
    return jsonify({'msg': 'nothing'})

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
    #idx = db.board.insert_one(doc)
    #print(idx)

    return jsonify({'msg':'저장완료'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)