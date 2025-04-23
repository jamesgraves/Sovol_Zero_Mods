import cadquery as cq


cone = (cq.Workplane("XY")
          .circle(2.15)
          .workplane(offset=14.0)
          .circle(2.15)
          .loft(combine=True)
          .faces(">Z")
          .circle(2.15)
          .workplane(offset=14)
          .circle(1.95)
          .loft(combine=True)
          )

result = (cq.Workplane("XY")
          .polygon(6, 7.0)
          .extrude(30)
          .faces("<Z")
          .cut(cone))

show_object(result)
result.export("bowden_cap.stl")