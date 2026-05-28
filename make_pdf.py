from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

pdfmetrics.registerFont(TTFont('IPAGothic', '/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf'))

text = """「純粋知性による思考」という概念が難しかった。感覚や想像を取り除いた思考とはどのようなものなのか、なかなかイメージできなかった。感覚も想像も使わずに何かを考えるとは、具体的にどういう状態なのだろうか。日常の思考は常に何らかのイメージや感覚と結びついているように思うので、純粋に知性だけで思考するという境地が自分にはまだ理解しきれなかった。次に、イデアが魂に生得的に備わっているというプラトンの考え方には違和感を覚えた。なぜなら、子供のころは知らないことばかりであり、数の概念や言語のルールも、成長の過程で少しずつ学び、獲得していくものだと感じるからだ。最初から魂に宿っているというよりも、経験や教育を通じて身につけていくものと感じた。また、哲人王の議論における「支配を望まない人が最良の支配者になる」という考えも、理想としては理解できるものの、現実にはそのような人物が権力の座に就くことはほとんどないと感じた。現実の政治では、権力を強く望む人間こそが支配者の地位を手に入れることが多い。"""

output_path = '/home/user/hello/output.pdf'

page_width, page_height = A4
margin_left = 25 * mm
margin_right = 25 * mm
margin_top = 30 * mm
margin_bottom = 25 * mm
font_size = 11
line_height = font_size * 1.8
usable_width = page_width - margin_left - margin_right

def wrap_by_width(text, font_name, font_size, max_width):
    """stringWidth で実際の幅を測りながら折り返す"""
    lines = []
    while text:
        lo, hi = 1, len(text)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if pdfmetrics.stringWidth(text[:mid], font_name, font_size) <= max_width:
                lo = mid
            else:
                hi = mid - 1
        lines.append(text[:lo])
        text = text[lo:]
    return lines

indented = '　　' + text
lines = wrap_by_width(indented, 'IPAGothic', font_size, usable_width)

c = canvas.Canvas(output_path, pagesize=A4)
c.setFont('IPAGothic', font_size)

y = page_height - margin_top
for line in lines:
    if y < margin_bottom + line_height:
        c.showPage()
        c.setFont('IPAGothic', font_size)
        y = page_height - margin_top
    c.drawString(margin_left, y, line)
    y -= line_height

c.save()
print(f"PDF saved to {output_path}")
