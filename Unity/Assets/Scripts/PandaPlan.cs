using System;
// using System.Range;
// using System.Index;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using RosMessageTypes.Geometry;
using RosMessageTypes.PandaMove;
using RosMessageTypes.Moveit;
using Unity.Robotics.ROSTCPConnector;
using Unity.Robotics.ROSTCPConnector.ROSGeometry;

public class PandaPlan : MonoBehaviour
{
    private ROSConnection ros;
    private string rosServiceName = "panda_plan";
    private string rosTopicName = "execution_check";
    private int nRobotJoints = 8;
    private float timeCheck;
    public GameObject panda;
    public ArticulationBody[] jointArticulationBodies;
    private RosMessageTypes.Trajectory.MJointTrajectoryPoint[] tempTrajectory;
    private int trajectoryIndex;
    
    // Start is called before the first frame update
    void Start()
    {
        ros = ROSConnection.instance;
        // ros2 = ROSConnection.instance;
        jointArticulationBodies = InitSync.jointArticulationBodies;
        panda = GameObject.Find("panda");

        ros.ImplementService<MPlanRequest>(rosServiceName, GetTrajectory);
        // ros2.RegisterPublisher<MExecutionCheck>(rosTopicName);
        ros.RegisterPublisher(rosTopicName, "panda_move/ExecutionCheck");

        Debug.Log("panda_plan server ON");
    }

    private MPlanResponse GetTrajectory(MPlanRequest request)
    {
        MPlanResponse response = new MPlanResponse();
        try
        {
            if (request.trajectories != null)
            {
                Debug.Log("Received Panda Plan Trajectory");
            }
            var tempTrajectory = request.trajectories[0].joint_trajectory.points;
            StartCoroutine(ExecuteTrajectory(tempTrajectory));
            response.execute_state = 1;
            return response;
        }
        catch (Exception ex)
        {
            Debug.Log("Trajectory Execution Error Occured");
            Debug.Log(ex);
            response.execute_state = 0;
            return response;
        }
    }
    private IEnumerator ExecuteTrajectory(RosMessageTypes.Trajectory.MJointTrajectoryPoint[] tempTrajectory)
    {
        for (int trajectoryIndex = 0; trajectoryIndex < tempTrajectory.Length; trajectoryIndex++)
        {
            var jointPosition = tempTrajectory[trajectoryIndex].positions;
            var jointVelocity = tempTrajectory[trajectoryIndex].velocities;
            var jointAcceleration = tempTrajectory[trajectoryIndex].accelerations;

            float[] convertedPosition = jointPosition.Select(r => (float)r * Mathf.Rad2Deg).ToArray();
            float [] convertedVelocity = jointVelocity.Select(r => (float)r * Mathf.Rad2Deg).ToArray();
            float [] convertedAcceleration = jointAcceleration.Select(r => (float)r * Mathf.Rad2Deg).ToArray();

            var rail1XDrive = jointArticulationBodies[0].xDrive;
            rail1XDrive.target = (float)jointPosition[0];
            jointArticulationBodies[0].xDrive = rail1XDrive;
            // jointArticulationBodies[0].jointVelocity = new ArticulationReducedSpace((float)jointVelocity[0]);
            // jointArticulationBodies[0].jointAcceleration = new ArticulationReducedSpace((float)jointAcceleration[0]);

            for (int jointIndex = 1; jointIndex < nRobotJoints; jointIndex++)
            {
                var joint1XDrive = jointArticulationBodies[jointIndex].xDrive;
                joint1XDrive.target = convertedPosition[jointIndex];
                jointArticulationBodies[jointIndex].xDrive = joint1XDrive;
                // jointArticulationBodies[jointIndex].jointVelocity = new ArticulationReducedSpace((float)convertedVelocity[jointIndex]);
                // jointArticulationBodies[jointIndex].jointAcceleration = new ArticulationReducedSpace((float)convertedAcceleration[jointIndex]);
            }
            yield return new WaitForSeconds(0.000001f);
        }
        Debug.Log("Trajectory Execution Completed");
        yield return new WaitForSeconds(0.3f);
        MExecutionCheck executionMSG = new MExecutionCheck();
        executionMSG.status = 1;
        ros.Send(rosTopicName, executionMSG);
    }
    // Update is called once per frame
    void Update()
    {

    }
}
