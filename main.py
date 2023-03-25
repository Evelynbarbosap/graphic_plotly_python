import plotly.graph_objects as go


class Main:
    # function for values static
    @staticmethod
    def build_chart_values_statics():
        x2 = [
            "08/03",
            "09/03",
            "11/03",
            "12/03",
            "13/03",
            "14/03",
            "15/03"
        ]

        y2 = [
            63868,
            55904,
            58144,
            62764,
            79645,
            43629,
            25269
        ]

        chart_colors = [
            'rgb(253, 236, 236)',  # rosa claro
            'rgb(255, 251, 235)',  # amarelo claro
            'rgb(230, 244, 247)',  # azul claro
            'rgb(255, 247, 237)',  # laranja claro
            'rgb(253, 236, 236)'  # rosa claro
        ]

        line_colors = [
            'rgb(239, 68, 68)',
            'rgb(245, 158, 11)',
            'rgb(8, 145, 178)',
            'rgb(249, 115, 22)'
        ]

        fig2 = go.Figure(layout={'paper_bgcolor': 'rgba(0,0,0,0)', 'plot_bgcolor': 'rgba(0,0,0,0)',
                                 'showlegend': True, })

        fig2.add_trace(go.Bar(x=[x2[0], x2[1]], y=[y2[0], y2[1]], marker=dict(
            color=chart_colors[0],
            line=dict(color=line_colors[0], width=2)
        )))

        fig2.add_trace(go.Bar(x=[x2[2]], y=[y2[2]], marker=dict(
            color=chart_colors[1],
            line=dict(color=line_colors[1], width=2)
        )))

        fig2.add_trace(go.Bar(x=[x2[3]], y=[y2[3]], marker=dict(
            color=chart_colors[2],
            line=dict(color=line_colors[2], width=2)
        )))

        fig2.add_trace(go.Bar(x=[x2[4]], y=[y2[4]], marker=dict(
            color=chart_colors[3],
            line=dict(color=line_colors[3], width=2)
        )))

        fig2.add_trace(go.Bar(x=[x2[5], x2[6]], y=[y2[5], y2[6]], marker=dict(
            color=chart_colors[4],
            line=dict(color=line_colors[0], width=2)
        )))

        # Customize aspect
        fig2.show()

    @staticmethod
    def check_eps_and_add_color(i, colors_line, colors_chart):
        data = {
            int(i) <= 25269: Main.__add_blue(colors_line, colors_chart),
            25269 < int(i) <= 55904: Main.__add_yellow(colors_line, colors_chart),
            55904 < int(i) <= 58144: Main.__add_orange(colors_line, colors_chart),
            int(i) > 58144: Main.__add_red(colors_line, colors_chart),
            None: 'rgb(0,0,0)'
        }

        resolver_response = data.get(i)
        return resolver_response

    @staticmethod
    def __add_blue(colors_line, colors_chart):
        colors_line.append('rgb(230, 244, 247)')
        colors_chart.append('rgb(8, 145, 178)')

        return colors_line, colors_chart

    @staticmethod
    def __add_yellow(colors_line, colors_chart):
        colors_line.append('rgb(245, 158, 11)')
        colors_chart.append('rgb(255, 251, 235)')

        return colors_line, colors_chart

    @staticmethod
    def __add_orange(colors_line, colors_chart):
        colors_line.append('rgb(249, 115, 22)')
        colors_chart.append('rgb(255, 247, 237)')

        return colors_line, colors_chart

    @staticmethod
    def __add_red(colors_line, colors_chart):
        colors_line.append('rgb(239, 68, 68)')
        colors_chart.append('rgb(253, 236, 236)')

        return colors_line, colors_chart

    # function for values dinamic
    @staticmethod
    def build_chart_eps():
        x2 = ["08/03", "09/03", "11/03", "12/03", "13/03", "14/03", "15/03"]
        y2 = [63868, 55904, 58144, 62764, 79645, 43629, 25269]
        colors_line = []
        colors_chart = []

        fig2 = go.Figure(data=[go.Bar(x=x2, y=y2)],
                         layout={'paper_bgcolor': 'rgba(0,0,0,0)', 'plot_bgcolor': 'rgba(0,0,0,0)',
                                 'showlegend': True, })

        for i in y2:
            Main.check_eps_and_add_color(i=i, colors_line=colors_line, colors_chart=colors_chart)

            fig2.update_layout(legend=dict(x=0.46, orientation="h"), margin_t=0, margin_r=0, margin_l=0, font_size=25)

            fig2.update_traces(name="Total events", marker_color=colors_chart, marker_line_color=colors_line,
                               marker_line_width=2.5)

        fig2.show()


if __name__ == '__main__':
    Main.build_chart_eps()
    # Main.build_chart_values_statics()
