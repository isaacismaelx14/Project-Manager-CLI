import React from "react";
import "@testing-library/jest-dom";
import { render } from "@testing-library/react";
import Test3 from "./";
describe("<Test3 />", () => {
  let component;
  beforeEach(() => {
    component = render(<Test3 />);
  });
  test("should render", () => {
    component.getByText("Test3");
  });
});