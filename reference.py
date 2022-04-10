toggle_2d = [["わ","を","ん","ゎ","ー","～","、","。","?","!"],
            ["あ","い","う","え","お"],
            ["か","き","く","け","こ"],
            ["さ","し","す","せ","そ"],
            ["た","ち","つ","て","と","っ"],
            ["な","に","ぬ","ね","の"],
            ["は","ひ","ふ","へ","ほ",],
            ["ま","み","む","め","も"],
            ["や","ゆ","よ","ゃ","ゅ","ょ"],
            ["ら","り","る","れ","ろ"]]

toggle_2d_dakuon = [["None","None","None","None","None"],
                 ["ぁ","ぃ","ぅ","ぇ","ぉ"],
                 ["が","ぎ","ぐ","げ","ご"],
                 ["ざ","ざ","じ","ず","ぞ"],
                 ["だ","ぢ","づ","で","ど"],
                 ["ば","び","ぶ","べ","ぼ",]]

toggle_2d_handakuon = [["null","null","null","null","null",],
                      ["null","null","null","null","null",],
                      ["null","null","null","null","null",],
                      ["null","null","null","null","null",],
                      ["null","null","null","null","null",],
                      ["null","null","null","null","null",],
                      ["ぱ","ぴ","ぷ","ぺ","ぽ"]]


def change(m,count):
    ss = toggle_2d[int(m)][count]
    return ss

def change_dakuon(m,count):
    ss = toggle_2d_dakuon[int(m)][count]
    return ss

def change_handakuon(m,count):
    ss = toggle_2d_handakuon[int(m)][count]
    return ss
    
