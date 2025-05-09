import cadquery as cq

baseplate = (cq.Workplane("XY")
     .box(95, 130, 3.0)
     .edges("|Z")
     .fillet(3.0)
     .faces(">Z")
     .workplane()
     .hole(79.0)
     .faces(">Z")
     .workplane(origin=(-33.5,-41))
     .hole(6.0)
     .faces(">Z")
     .workplane(origin=(33.5,-41))
     .hole(6.0)
     )

cone = (cq.Workplane("XY")
      .circle(43.0)
      .workplane(offset=60.0)
      .circle(59.0)
      .loft(combine=True)
      .faces("+Z or -Z")
      .faces(">Z")
      .workplane()
      .hole(79)
      )

cyl = (cq.Workplane("XY")
       .circle(59.0)
       .workplane(offset=70)
       .circle(59.0)
       .loft(combine=True)
       .faces("+Z or -Z")
       .shell(-3)
       )

#         .add(cone, loc=cq.Location(cq.Vector(0, 0, 0)))
#        .add(cyl,   loc=cq.Location(cq.Vector(0, 0, 0)))

result = (
        cq.Assembly(baseplate, loc=cq.Location(cq.Vector(0, 0, 0)))
        .add(cone, loc=cq.Location(cq.Vector(0, 0, 0)))
        .add(cyl,   loc=cq.Location(cq.Vector(0, 0, 60)))
        )

show_object(result)
result.export("exhaust_adapter.stl")
