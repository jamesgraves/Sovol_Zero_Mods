import cadquery as cq

glass_top = (
    cq.Workplane("XY")
    .workplane(offset=-15.0)
    .move(138.5, 138.5)
    .box(277.0, 277.0, 4.0)
    )

show_object(glass_top)

filter = (
    cq.Workplane("XY")
    .workplane(offset=+60.0)
    .move(138.5, 138.5)
    .box(247.65, 247.65, 22)
    )

show_object(filter)

triangle = [
    (0,0),
    (0,30),
    (30,30),
    (0,0),
    ]

angle_cut = (
    cq.Workplane("XY")
    .polyline(triangle)
    .consolidateWires()
    .extrude(30)
    )

triangle2 = [
    (0,0),
    (30,0),
    (30,30),
    (0,0),
    ]

angle_cut2 = (
    cq.Workplane("XY")
    .polyline(triangle2)
    .consolidateWires()
    .extrude(30)
    )

adapter_biscuit = (
        cq.Workplane("XY")
        .box(20, 9.5, 3.00)
        )

adapter_biscuit.export("adapter_biscuit.step")

adapter_shape = [
    (4,4),
    (0, 4),
    (0, 0),
    (9,0),
    (9,10),
    (12.175,10),
    (12.175,0),
    (29.675, 0),
    (29.675, 4),
    (14.675, 4),
    (14.675, 24),
    (10.675, 24),
    (4,4)
    ]

adapt_side1 = (
    cq.Workplane("YZ")
    .polyline(adapter_shape)
    .consolidateWires()
    .extrude(139.7)
    .faces("<X")
    .cut(angle_cut)
    )

show_object(adapt_side1)

adapt_side2 = (
    cq.Workplane("XZ")
    .polyline(adapter_shape)
    .consolidateWires()
    .extrude(-139.7)
    .faces("<Y")
    .cut(angle_cut2)
    )

show_object(adapt_side2)

result = (
    cq.Assembly(adapt_side1).add(adapt_side2))
result.export("filter_adapter.step")

