from quantifyx.hydraulics.pipe import calculate_pipe_headloss


def test_hydraulics_pipe_api():
    result = calculate_pipe_headloss(
        length_m=100,
        diameter_m=0.2,
        flow_m3s=0.01,
        roughness_m=0.0002,
        kinematic_viscosity=1e-6,
    )

    assert result["headloss"] > 0