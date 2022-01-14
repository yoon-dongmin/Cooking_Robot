using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using RosMessageTypes.Geometry;
using RosMessageTypes.PandaMove;
using Unity.Robotics.ROSTCPConnector;
using Unity.Robotics.ROSTCPConnector.ROSGeometry;

public class SceneSync : MonoBehaviour
{
    private ROSConnection ros;
    private int nRobotJoints = 10;
    private string rosServiceName = "scene_sync";
    private string[] activatedObjectList;
    private double[] jointStates = new double[10];
    private MPoint[] objectPositions;
    private MQuaternion[] objectOrientations;
    public ArticulationBody[] jointArticulationBodies;

    // Start is called before the first frame update
    void Start()
    {
        ros = ROSConnection.instance;

        jointArticulationBodies = InitSync.jointArticulationBodies;

        ros.ImplementService<MSyncRequest>(rosServiceName, SendObjectPose);

        Debug.Log("scene_sync server ON");
    }

    private MSyncResponse SendObjectPose(MSyncRequest request)
    {
        Debug.Log("Received Scene Update Request");

        MSyncResponse response = new MSyncResponse();
        try
        {
            activatedObjectList = request.activated_object;

            for (int jointIndex = 0; jointIndex < nRobotJoints; jointIndex++)
            {
                jointStates[jointIndex] = jointArticulationBodies[jointIndex].xDrive.target;
            }
            response.joint_state = jointStates;

            response.object_name = activatedObjectList;

            objectPositions = new MPoint[activatedObjectList.Length];
            objectOrientations = new MQuaternion[activatedObjectList.Length];

            for (int objectIndex = 0; objectIndex < activatedObjectList.Length; objectIndex++)
            {
                GameObject targetObject = GameObject.Find(activatedObjectList[objectIndex]);
                // response.object_name[ObjectIdx] = ObjectList[ObjectIdx];
                // response.position[ObjectIdx] = TargetObject.transform.position.To<FLU>();
                // response.position.Add(TargetObject.transform.position.To<FLU>());
                // response.orientation[ObjectIdx] = TargetObject.transform.rotation.To<FLU>();
                objectPositions[objectIndex] = targetObject.transform.position.To<FLU>();
                objectOrientations[objectIndex] = (targetObject.transform.rotation * Quaternion.Euler(0, -90, 0)).To<FLU>(); // CHECK
            }

            response.position = objectPositions;
            response.orientation = objectOrientations;

            Debug.Log("Scene Update Response Success");
            return response;
        }
        
        catch (Exception ex)
        {
            Debug.Log(ex);

            return response;
        }
    }

    // Update is called once per frame
    void Update()
{

}
}
