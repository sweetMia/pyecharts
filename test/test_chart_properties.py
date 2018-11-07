#!/usr/bin/env python
# coding=utf-8

from __future__ import unicode_literals

from test.constants import CLOTHES, WEEK

from nose.tools import eq_

from pyecharts import Bar, Grid, Line
from pyecharts.base import Base

UUID_HEX_LENGTH = 32


def test_base_properties():
    b = Base()
    eq_(len(b.chart_id), UUID_HEX_LENGTH)
    eq_(b.width, '800px')
    eq_(b.height, '400px')
    eq_(len(b.options), 0)  # empty
    assert ("echarts" in b.js_dependencies) or (
        "echarts.min" in b.js_dependencies
    )


def test_chart_properties():
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图-数据堆叠示例", width='900px', height='500px')
    bar.add("商家A", CLOTHES, v1, is_stack=True)
    bar.add("商家B", CLOTHES, v2, is_stack=True)

    eq_(len(bar.chart_id), UUID_HEX_LENGTH)
    eq_(bar.width, '900px')
    eq_(bar.height, '500px')
    assert ("echarts" in bar.js_dependencies) or (
        "echarts.min" in bar.js_dependencies
    )


def test_grid_properties():
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图示例", height='720px')
    bar.add("商家A", CLOTHES, v1, is_stack=True)
    bar.add("商家B", CLOTHES, v2, is_stack=True)
    line = Line("折线图示例", title_top="50%")
    line.add(
        "最高气温",
        WEEK,
        [11, 11, 15, 13, 12, 13, 10],
        mark_point=["max", "min"],
        mark_line=["average"],
    )
    line.add(
        "最低气温",
        WEEK,
        [1, -2, 2, 5, 3, 2, 0],
        mark_point=["max", "min"],
        mark_line=["average"],
        legend_top="50%",
    )

    grid = Grid(width='1024px', height='768px')
    grid.add(bar, grid_bottom="60%")
    grid.add(line, grid_top="60%")
    eq_(grid.width, '1024px')
    eq_(grid.height, '768px')
    assert ("echarts" in bar.js_dependencies) or (
        "echarts.min" in bar.js_dependencies
    )
