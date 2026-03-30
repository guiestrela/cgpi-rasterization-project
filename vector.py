import cairo

def cria_imagem_vetorial():
    surface = cairo.SVGSurface("outputs/vector.svg", 500, 500)
    ctx = cairo.Context(surface)

    # Linha preta
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(100, 150)
    ctx.line_to(400, 350)
    ctx.stroke()

    # Linha cinza
    ctx.set_source_rgb(0.3, 0.3, 0.3)
    ctx.move_to(400, 150)
    ctx.line_to(100, 350)
    ctx.stroke()

    # Círculo
    ctx.set_source_rgb(0.8, 0.8, 0.8)
    ctx.arc(250, 250, 120, 0, 6.28)
    ctx.stroke()

    surface.finish()